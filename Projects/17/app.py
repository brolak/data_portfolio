import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from shiny import App, ui, render, reactive

try:
    df = pd.read_csv("visualizing_global_co2_data.csv")
except:
    path = "https://drive.google.com/file/d/16w_qjmvXFkPcR7tt4W1UKQC7ZIwgK8sR/view?usp=sharing"
    path = 'https://drive.google.com/uc?id=' + path.split('/')[-2]
    df = pd.read_csv(path)

iso_to_country = df.drop_duplicates(subset=['iso_code']).set_index('iso_code')['country'].to_dict()
iso_to_country_clean = {k: v for k, v in iso_to_country.items() if pd.notna(k)}

columns_to_keep = [
    'iso_code', 'year', 'population', 'gdp', 'co2', 'methane', 'nitrous_oxide',
    'total_ghg'
]
df = df[columns_to_keep]

COUNTRY = 'USA'
df_countries = df[df['iso_code'].notna()]

corr = df.select_dtypes(include='number').corr()

cumulative_ghg = df.groupby('iso_code', as_index=False)['co2'].sum()

top20_ghg = cumulative_ghg.sort_values('co2', ascending=False).head(20)

top20_ghg['country'] = top20_ghg['iso_code'].map(iso_to_country_clean)

POP_THRESHOLD = 60_000

df['total_co2_per_capita'] = df.apply(
    lambda row: row['co2'] / row['population'] if pd.notnull(row['co2']) and pd.notnull(row['population']) and row['population'] != 0 else None,
    axis=1
)

cumulative_ghg_per_capita = df.groupby('iso_code', as_index=False)['total_co2_per_capita'].sum()
top20_ghg_per_capita = cumulative_ghg_per_capita.sort_values('total_co2_per_capita', ascending=False).head(20)
top20_ghg_per_capita['country'] = top20_ghg_per_capita['iso_code'].map(iso_to_country_clean)
avg_pop = df.groupby('iso_code')['population'].mean()
valid_iso_codes = avg_pop[avg_pop > POP_THRESHOLD].index
filtered_top20 = top20_ghg_per_capita[top20_ghg_per_capita['iso_code'].isin(valid_iso_codes)]
filtered_top20 = filtered_top20.sort_values('total_co2_per_capita', ascending=False).head(20)

app_ui = ui.page_fluid(
    ui.h2("Global CO2 Emissions Dashboard"),
    ui.h4("Worldwide Average Trends"),
    ui.hr(),
    ui.output_plot("world_trends"),
    ui.hr(),
        ui.input_selectize(
        "country",
        "Select Country",
        choices={k: v for k, v in iso_to_country_clean.items()},
        selected=COUNTRY
    ),
    ui.hr(),
    ui.h4("Distribution of Features for Selected Country"),
    ui.output_plot("country_hist"),
    ui.hr(),
    ui.h4("Top 20 Countries by Cumulative CO2 Emissions"),
    ui.output_plot("top20_abs"),
    ui.hr(),
    ui.h4("Top 20 Countries by Cumulative CO2 Emissions Per Capita"),
    ui.output_plot("top20_percap")
)

def server(input, output, session):

    @output
    @render.plot
    def world_trends():
        fig, axs = plt.subplots(2, 3, figsize=(15, 8))
        columns = ['population', 'gdp', 'co2', 'methane', 'nitrous_oxide', 'total_ghg']
        for i, column in enumerate(columns):
            data = df_countries[df_countries[column].notna() & (df_countries[column] != 0)]
            ax = axs[i // 3, i % 3]
            sns.lineplot(
                data=data,
                x='year',
                y=column,
                estimator='mean',
                marker='o',
                ax=ax
            )
            ax.set_title(column)
        plt.tight_layout()
        return fig
    
    @reactive.Calc
    def selected_country():
        return input.country()

    @output
    @render.plot
    def country_hist():
        fig, axs = plt.subplots(2, 3, figsize=(15, 8))
        columns = ['population', 'gdp', 'co2', 'methane', 'nitrous_oxide', 'total_ghg']
        country = selected_country()
        for i, column in enumerate(columns):
            data = df[(df['iso_code'] == country) & df[column].notna() & (df[column] != 0)][column]
            ax = axs[i // 3, i % 3]
            sns.histplot(data, bins=30, kde=True, color='blue', ax=ax)
            ax.set_title(column)
        plt.tight_layout()
        return fig

    @output
    @render.plot
    def top20_abs():
        fig = plt.figure(figsize=(12, 6))
        sns.barplot(data=top20_ghg, x='country', y='co2',hue='country', legend=False, palette='viridis')
        plt.xticks(rotation=75)
        plt.xlabel('Country')
        plt.ylabel('Cumulative CO2 Emissions')
        plt.title('Top 20 Countries by CO2 Emissions')
        plt.tight_layout()
        return fig

    @output
    @render.plot
    def top20_percap():
        avg_pop_local = df.groupby('iso_code')['population'].mean()
        valid_iso_codes_local = avg_pop_local[avg_pop_local > POP_THRESHOLD].index
        filtered = filtered_top20[filtered_top20['iso_code'].isin(valid_iso_codes_local)]
        fig = plt.figure(figsize=(12, 6))
        sns.barplot(
            data=filtered,
            x='country',
            y='total_co2_per_capita',
            hue='country',
            legend=False,
            palette='viridis'
        )
        plt.xticks(rotation=75)
        plt.xlabel('Country')
        plt.ylabel('Cumulative CO2 Emissions Per Capita')
        plt.title(f'Top 20 Countries by Cumulative CO2 Emissions Per Capita (Population > {POP_THRESHOLD})')
        plt.tight_layout()
        return fig

app = App(app_ui, server)