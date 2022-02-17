## Data Summary:

The `weather` table:
- *start_ts* - pickup date and time
- *weather_conditions* - weather conditions at the moment the ride started
- *duration_seconds* - ride duration in seconds

The `company` table:
- *company_name* - taxi company name
- *trips_amount* - the number of rides for each taxi company on November 15-16, 2017

The `dropoff` table:
- *dropoff_location_name* - Chicago neighborhoods where rides ended
- *average_trips* - the average number of rides that ended in each neighborhood in November 2017.

## Goal:

You're working as an analyst for Zuber, a new ride-sharing company that's launching in Chicago. Your task is to find patterns in the available information. You want to understand passenger preferences and the impact of external factors on rides.

Working with a database, you'll analyze data from competitors and test a hypothesis about the impact of weather on ride frequency.

## Libraries used:

beautiful soup & SQL were used in data wrangling, pandas, numpy, scipy, matlibplot

[:snake: Jupyter Notebook](./Data_Collection_&_Storage.ipynb)