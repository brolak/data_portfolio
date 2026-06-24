## Data Summary:

Player preference data was synthetically generated for 200 players across 37 board game categories scraped from BoardGameGeek. Each player has a preference score (−1 to 1) for each category, representing their affinity for that genre.

- `Player` — unique player node in the network
- `Categories (×37)` — preference score per board game category (e.g. Abstract Strategy, Bluffing, Deduction...)
- `Compatibility Edge` — cosine similarity score between two players' preference vectors (threshold ≥ 0.5 to form an edge)

## Goal:

Model a board game night as a social network problem: represent players as nodes connected by weighted compatibility edges, then compare network-based algorithmic grouping against random grouping to measure the impact on participant satisfaction.

## Conclusion:

A greedy community detection algorithm was applied to the compatibility network and benchmarked against random groupings across 50 trials:

- Network-based grouping achieved **5–7% higher average compatibility scores** than random assignment
- Lower variance in network grouping indicates more consistent and reliable group formation
- An optimal compatibility threshold of **0.5** balances group quality with computational efficiency — lower thresholds dramatically increase computation time due to network density

## Libraries used:

networkx, pandas, numpy, matplotlib, requests, beautifulsoup4, itertools

[:snake: Jupyter Notebook](./SNA%20Final.ipynb)
