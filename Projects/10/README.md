## Data Summary:

__Features__:
- insured person's gender, age, salary, and number of family members.

__Target__: 
- number of insurance benefits received by an insured person over the last five years.

## Goal:

The Sure Tomorrow insurance company wants to solve several tasks with the help of Machine Learning, and you are asked to evaluate that possibility.

1. Find customers who are similar to a given customer. This will help the company's agents with marketing.
2. Predict whether a new customer is likely to receive an insurance benefit. Can a prediction model do better than a dummy model?
3. Predict the number of insurance benefits a new customer is likely to receive using a linear regression model.
4. Protect clients' personal data without breaking the model from the previous task.

It's necessary to develop a data transformation algorithm that would make it hard to recover personal information if the data fell into the wrong hands. This is called data masking, or data obfuscation. But the data should be protected in such a way that the quality of machine learning models doesn't suffer. You don't need to pick the best model, just prove that the algorithm works correctly.

## Libraries used:

seaborn, sklearn, pandas, numpy

[:snake: Python Notebook](./Linear Algebra.ipynb)