## Data Summary:

The dataset contains global fossil fuel emissions data from 1750–2021 by country, sourced from Our World in Data (CC BY 4.0) via MavenAnalytics:

- `iso_code` — ISO 3166-1 alpha-3 country code
- `year` — year of observation
- `population` — country population
- `gdp` — gross domestic product (USD)
- `co2` — CO2 emissions (million tonnes)
- `methane` — methane emissions (million tonnes CO2 equivalent)
- `nitrous_oxide` — nitrous oxide emissions (million tonnes CO2 equivalent)
- `total_ghg` — total greenhouse gas emissions (million tonnes CO2 equivalent)

The raw dataset contains 50,598 rows and 79 columns; analysis focuses on the 8 core features above.

## Goal:

Explore 270 years of global greenhouse gas emissions data to identify trends, correlations, and the countries most responsible for cumulative emissions — both in absolute terms and per capita.

Key findings:
- All major emission features have increased consistently over time, driven by industrialization and population growth.
- CO2, methane, nitrous oxide, population, and GDP are strongly correlated with each other.
- The USA, China, and Russia dominate cumulative absolute CO2 emissions.
- When normalized per capita, oil-producing nations (Qatar, Kuwait, UAE) and some smaller countries rank highest, highlighting the role of resource extraction and weaker environmental regulation.

An interactive Shiny for Python dashboard was built and deployed to allow exploration by country.

## Libraries used:

pandas, matplotlib, seaborn, shiny

[:snake: Jupyter Notebook](./ITDS_midterm.ipynb)
[:computer: Shiny App - deployed](https://brolak.shinyapps.io/globalco2/)
[:page_facing_up: App Source](./app.py)
