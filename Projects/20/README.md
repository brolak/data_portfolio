## Data Summary:

Synthetic call centre dataset containing 60,000 support call records from August–November 2025:

- `call_id` — unique call identifier
- `date` — date of the call
- `region` — service region (North, South, Center)
- `agent_id` — handling agent identifier
- `wait_time_sec` — customer wait time in seconds (4.3% missing)
- `call_duration_sec` — total call duration in seconds
- `issue_type` — type of issue reported (billing, technical, general)
- `system_version` — software version active at time of call (v1.0, v1.1, v1.2)
- `resolved` — whether the issue was resolved (1/0)
- `satisfaction` — customer satisfaction score (1–5)
- `customer_type` — free or premium customer

## Goal:

Investigate a decline in customer satisfaction and resolution rates observed in October–November to identify the root cause and affected segments.

## Conclusion:

- A system version switch from v1.1 to v1.2 was confirmed on **October 20th**
- v1.2 correlates with lower average satisfaction scores and a drop in resolution rates
- The decline was most pronounced for **premium customers** and customers in the **North region**
- **Billing issues** saw the sharpest satisfaction drop following the version change
- Wait times increased in mid-October, compounding the satisfaction decline
- Missing `wait_time_sec` values were concentrated in satisfaction = 1 customers, imputed using the 90th percentile of daily wait times for low-satisfaction calls

## Libraries used:

pandas, matplotlib, seaborn, sklearn

[:snake: Jupyter Notebook](./use-case-2-analysis.ipynb)
