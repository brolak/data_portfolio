## Data Summary:

- *date_posted* — the publication date.
- *days_listed* — how many days the ad was displayed (from publication to removal).
- *last_price* — the price at the time when the ad was removed (dollars).
- *bedrooms* — the number of bedrooms.
- *kitchen_area* — the kitchen area in square meters (sq.m.).
- *living_area* — the living area in square meters (sq.m.).
- *total_area* — the total area in square meters (sq.m.).
- *balconies* — the number of balconies.
- *ceiling_height* — the ceiling height in meters (m.).
- *floor* — the apartment floor number.
- *floors_total* — the total number of floors in the building.
- *bike_parking* — whether there is parking for bikes (Boolean type).
- *is_open_plan* — whether or not it has an open plan design (Boolean type).
- *is_studio* — whether or not it's a studio (Boolean type).
- *locality_name* — the locality name.
- *airport_dist* — the distance to the airport in meters (m.).
- *city_center_dist* — the distance to the city center in meters (m.).
- *park_dist* — the distance to the nearest park in meters (m.).
- *parks_within_3000* — the number of parks in a 3 km. radius.
- *pond_dist* — the distance to the nearest body of water (m.).
- *ponds_within_3000* — the number of bodies of water in a 3 km. radius.

## Goal:

You will have the data from a real estate agency. It is an archive of sales ads for realty in St. Petersburg, Russia, and the surrounding areas collected over the past few years. You’ll need to learn how to determine the market value of real estate properties. Your task is to define the parameters. This will make it possible to build an automated system that is capable of detecting anomalies and fraudulent activity.
There are two different types of data available for every apartment for sale. The first type is a user’s input. The second type is received automatically based upon the map data. For example, the distance from the city center, airport, the nearest park or body of water.

## Libraries used:

pandas

[:snake: Jupyter Notebook](./Exploratory_Data_Analysis.ipynb)