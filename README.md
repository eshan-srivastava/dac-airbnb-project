# Problem Statement 
Airbnb, Inc. is an American company that operates an online marketplace for lodging, primarily homestays for vacation rentals, and tourism activities. Based in San Francisco, California, Airbnb does not own any of the listed properties; instead, it profits by receiving commission from each booking. Since NYC is a dense human traffic spot, hotels and lodgings are very much in business. Thus, being able to know (**predict**) the price of Airbnb listings is useful.
You can go check out the [yet-to-be-published accompanying blog](https://docs.google.com/document/d/12g8DamUO5uQF68cjOk2lYQbQZf62FXk-qs04JT0voRo/edit?usp=sharing)

## Dataset

The dataset used is the [New York City Airbnb Open Data](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data) from Kaggle. It contains Airbnb listings and metrics in NYC, NY, USA (2019).

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
# Ridge Regression
Ridge Regression is a popular type of regularized linear regression that includes an L2 penalty. This has the effect of shrinking the coefficients for those input variables that do not contribute much to the prediction task. An L2 penalty minimizes the size of all coefficients, although it prevents any coefficients from being removed from the model by allowing their value to become zero. A hyperparameter is used called “lambda” that controls the weighting of the penalty to the loss function. A default value of 1.0 will fully weight the penalty; a value of 0 excludes the penalty. Very small values of lambda, such as 1e-3 or smaller are common.
The assumptions of ridge regression are the same as that of linear regression: linearity, constant variance, and independence. However, as ridge regression does not provide confidence limits, the distribution of errors to be normal need not be assumed.

# Decision Tree Regression
Decision tree builds regression or classification models in the form of a tree structure. It breaks down a dataset into smaller and smaller subsets while at the same time an associated decision tree is incrementally developed. The final result is a tree with decision nodes and leaf nodes. It is a tree-structured classifier, where internal nodes represent the features of a dataset, branches represent the decision rules and each leaf node represents the outcome. In a Decision tree, there are two nodes, which are the Decision Node and Leaf Node. Decision nodes are used to make any decision and have multiple branches, whereas Leaf nodes are the output of those decisions and do not contain any further branches.
The decisions or the test are performed on the basis of features of the given dataset.

# Random Forest Regression
Random Forest Regression is a supervised learning algorithm that uses ensemble learning method for regression. Ensemble learning method is a technique that combines predictions from multiple machine learning algorithms to make a more accurate prediction than a single model. Instead of relying on one decision tree, the random forest takes the prediction from each tree and based on the majority votes of predictions, and it predicts the final output.
The greater number of trees in the forest leads to higher accuracy and prevents the problem of overfitting. 

Since the random forest combines multiple trees to predict the class of the dataset, it is possible that some decision trees may predict the correct output, while others may not. But together, all the trees predict the correct output. Therefore, below are two assumptions for a better Random forest classifier:
1. There should be some actual values in the feature variable of the dataset so that the classifier can predict accurate results rather than a guessed result.
2. The predictions from each tree must have very low correlations.
<br>


## Future Work
We plan to use **Residual Plots** to improve accuracy of our regression models. We can implement classification algorithms and expand our prediction model to predict neighbourhoods in NYC to have a vacation in.

