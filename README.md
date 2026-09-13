# Combined Cycle Power Plant Power Output Prediction

## 1. Objectives

* To predict the **electrical power output (PE)** of a Combined Cycle Power Plant.
* To investigate the relationship between PE and **Ambient Temperature (AT), Exhaust Vacuum (V), Ambient Pressure (AP), and Relative Humidity (RH)**.
* To develop and compare different regression and machine-learning models.
* To determine whether more complex nonlinear models provide better predictive performance than Multiple Linear Regression.

## 2. Methodology

* The four predictor variables were **standardized using StandardScaler**.
* The dataset was divided into **training and testing sets in an 80:20 ratio**.
* The following models were developed:

  * Multiple Linear Regression
  * Polynomial Regression
  * Regression Tree
  * XGBoost Regression
  * Feed-Forward Artificial Neural Network (ANN)
* The ANN consisted of **two hidden layers**, with **ReLU (Rectified Linear Unit)** activation in the hidden layers and a **linear activation function** in the output layer.
* All models were evaluated using the same test data.

## 3. Performance Evaluation

The models were evaluated using R².

### R² — Coefficient of Determination

R² measures the proportion of variation in electrical power output explained by the model. A higher R² indicates better performance.

The obtained R² values were approximately:

| Model                      |                           R² |
| -------------------------- | ---------------------------: |
| Multiple Linear Regression |                    **94.54%** |
| Polynomial Regression      |                    **94.58%**|
| Regression Tree            |                   **93.51%** |
| XGBoost Regression         |                    **94.6%** |
| Feed-Forward ANN           |                    **93.9%** |

The models produced **very similar R² values**, indicating that all models were able to explain a large proportion of the variation in electrical power output.

Multiple Linear Regression explained approximately **94.5% of the variation** in PE using AT, V, AP, and RH.

Polynomial Regression did not produce a substantial improvement over Multiple Linear Regression, suggesting that the additional polynomial terms did not contribute much additional explanatory power.

XGBoost achieved the highest R² of approximately **94.6%**, but the improvement over Multiple Linear Regression was very small.

The ANN achieved an R² of approximately **93.9%**, showing good predictive ability but no substantial improvement over the simpler models.

## 4. Conclusion

The comparison shows that **all the models achieved high and relatively similar predictive performance**.

Although XGBoost produced the highest R² of approximately **94.6%**, its improvement over Multiple Linear Regression was marginal. Multiple Linear Regression achieved an R² of **94.5%** while providing a much simpler and more interpretable model.

The ANN was able to model nonlinear relationships, but its performance did not substantially exceed that of the traditional regression models.

Therefore, the results suggest that **increasing model complexity does not necessarily lead to a significant improvement in prediction for this dataset**. Since Multiple Linear Regression provides comparable performance with greater simplicity and interpretability, it can be considered a suitable practical model for predicting electrical power output.
