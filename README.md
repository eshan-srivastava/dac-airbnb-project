# Problem Statement 
This should be a brief description of the domain of your dataset (e.g. if it is the Titanic Dataset then write about the ship, the incident that happened, what you're trying to do with the data). You can go check out the accompanying blog, [link to be put]

## Dataset

The dataset used is the [New York City Airbnb Open Data](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data) from Kaggle. 

**Target Variable: Price (in dollars)**
<br>
<br>
Price refers to the price for the Airbnb listing.
<br>
**Mean Listing Price:** 153$
<br>
**Max Listing Price:** 10,000$
<br>
**Min Listing Price:** 0
<br>
**Standard Deviation:** 240
<br>
**3rd Quartile:** 175$

Given the input of some parameters (like room type, nights to stay) we can predict the Target Variable and thus recommend listings based on price that the model predicts. 
## Model(s) Used

We have plans to use regression models as of now: 
# Linear Regression 
Linear Regression is the supervised Machine Learning model in which the model finds the best fit linear line between the independent and dependent variable i.e it finds the linear relationship between the dependent and independent variable. This regression technique finds out a linear relationship between x (input) and y(output). Hence, the name is Linear Regression. The typical equation of a line is y = mx + a, where m is the slope, x is independent variable and y is dependent variable that we are interested in predicting
# Lasso Regression
Lasso regression is a regularization technique. It is used over regression methods for a more accurate prediction. This model uses shrinkage. Shrinkage is where data values are shrunk towards a central point as the mean. The lasso procedure encourages simple, sparse models (i.e. models with fewer parameters). This particular type of regression is well-suited for models showing high levels of multicollinearity or when you want to automate certain parts of model selection, like variable selection/parameter elimination.
# K Cross Validation for validation
Cross-validation is a resampling procedure used to evaluate machine learning models on a limited data sample. 
<br>


## Future Work
We can implement classification algorithms and expand our prediction model to predict neighbourhoods in NYC to have a vacation in.

