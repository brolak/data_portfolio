## Data Summary:

IBM HR Analytics employee dataset containing 1,470 records across 33 features. Target variable is `MonthlyIncome`.

- `JobLevel` — primary salary predictor (1–5 scale)
- `JobRole`, `Department` — role and department classification
- `TotalWorkingYears`, `YearsAtCompany`, `YearsInCurrentRole` — tenure features
- `MonthlyIncome` — target variable (mean $6,503, range $1,009–$19,999)
- Additional satisfaction, demographic, and compensation features

## Goal:

Build a linear regression model to predict employee salary, then perform regression error analysis to understand how and why the model makes mistakes — and whether those mistakes are random or systematic.

## Conclusion:

- The model achieves **R² = 0.94** on the training set, but MAE = **$852/month** (~13% of average salary) on the test set
- Errors are **systematic, not random**: the model predicts JobLevel midpoints rather than continuous salaries, creating discrete vertical residual clusters
- Error grows with seniority: Job Level 4–5 employees have 2–3× higher MAE than Level 1–2
- The 3 worst predictions were all Level 2 employees paid at Level 4–5 rates — within-level salary variation the model has no features to capture
- A log-transform of the target made errors worse, not better
- The model is reliable as a diagnostic tool (flagging pay divergence from job-level structure) but should not be used to set individual salaries for Managers and Directors

## Libraries used:

pandas, numpy, matplotlib, seaborn, sklearn, statsmodels

[:snake: Jupyter Notebook](./use-case-1-analysis.ipynb)
