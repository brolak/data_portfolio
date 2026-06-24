## Data Summary:

The dataset consists of 5,000 e-commerce transactions from Q4 2024 (October–December):

- `Transaction_ID` — unique transaction identifier
- `Customer_ID` — unique customer identifier
- `Gender` — customer gender
- `Purchase_Date` — date of transaction
- `Items_Purchased` — number of items purchased (0 indicates abandoned session)
- `Total_Spent` — total amount spent
- `Category` — product category purchased (null for abandoned sessions)
- `Session_Duration` — duration of the shopping session in minutes
- `Hour` — hour of day the session occurred
- `Has_Children` — whether the customer has children (1 = yes, 0 = no)
- `Payment_Method` — payment method used (null for abandoned sessions)
- `Checkout_Time` — time spent at checkout in minutes

## Goal:

Analyze customer transaction data to identify cart abandonment patterns, uncover underperforming segments, and simulate the revenue impact of targeted retention solutions.

Two solutions were proposed and simulated:

1. **Children's segment campaign** — customers with children had a ~5% conversion rate vs. ~59% for those without. A targeted campaign was simulated to bring their rate to parity.
2. **Checkout time reduction** — customers spending more than 4 minutes at checkout were disproportionately abandoning. Reducing checkout friction was simulated for this group.

Combined, the two solutions reduced the abandonment rate from ~46% to ~15% and nearly doubled total sales from $808K to $1.5M.

## Libraries used:

pandas, numpy, matplotlib, seaborn

[:snake: Jupyter Notebook](./STIDI%20Final%20Analysis.ipynb)
[:page_facing_up: Presentation](./Final%20Presentation.pdf)
