## Data Summary:

The IBM HR Analytics Employee Attrition dataset contains 1,470 employee records across 35 features:

- `Attrition` — whether the employee left the company (Yes/No) — target variable
- `Age`, `Gender`, `MaritalStatus` — employee demographics
- `Department`, `JobRole`, `JobLevel` — role and department information
- `MonthlyIncome`, `DailyRate`, `HourlyRate`, `StockOptionLevel` — compensation features
- `JobSatisfaction`, `EnvironmentSatisfaction`, `WorkLifeBalance`, `JobInvolvement` — satisfaction scores (1–4)
- `YearsAtCompany`, `TotalWorkingYears`, `YearsInCurrentRole`, `YearsSinceLastPromotion` — tenure features
- `OverTime`, `BusinessTravel`, `NumCompaniesWorked`, `TrainingTimesLastYear` — work pattern features

## Goal:

Identify the key demographic, compensation, and satisfaction drivers of employee attrition, with a focused deep-dive into the Sales Representative role.

## Conclusion:

- Overall attrition rate is ~16%, with Sales Representatives showing significantly higher attrition than other roles
- Employees with no stock options (Level 0) had the highest attrition rates across all job and satisfaction levels
- Lower job involvement, lower income, and younger age were consistently associated with higher attrition
- Attriting employees cluster at the low end of the Age vs. Monthly Income distribution, suggesting early-career, lower-paid employees are most at risk
- Work-life balance and environment satisfaction compound the effect of stock option level on attrition

## Libraries used:

pandas, numpy, matplotlib, seaborn

[:snake: Jupyter Notebook](./Usecase%201%20Analysis.ipynb)
