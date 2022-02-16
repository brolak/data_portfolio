## Data Summary:

- *сalls* — number of calls
- *minutes* — total call duration in minutes
- *messages* — number of text messages
- *mb_used* — Internet traffic used in MB
- *is_ultra* — plan for the current month (Ultra - 1, Smart - 0)

## Goal:

Mobile carrier Megaline has found out that many of their subscribers use legacy plans. They want to develop a model that would analyze subscribers' behavior and recommend one of Megaline's newer plans: Smart or Ultra.

You have access to behavior data about subscribers who have already switched to the new plans (from the project for the Statistical Data Analysis course). For this classification task, you need to develop a model that will pick the right plan. Since you’ve already performed the data preprocessing step, you can move straight to creating the model.

Develop a model with the highest possible accuracy. In this project, the threshold for accuracy is 0.75. Check the accuracy using the test dataset.

## Libraries used:

sklearn, pandas, matlibplot