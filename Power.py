import pandas as pd
import numpy as np
import tensorflow as tf

tf.__version__

dataset=pd.read_excel('Folds5x2_pp.xlsx')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values
print(X)
print(y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test=sc.fit_transform(X_test)

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
X_train_poly = poly_reg.fit_transform(X_train)
X_test_poly = poly_reg.transform(X_test)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_train_poly, y_train)

y_pred = lin_reg_2.predict(X_test_poly)

r2 = r2_score(y_test, y_pred)
print(r2)

from sklearn.tree import DecisionTreeRegressor

tree = DecisionTreeRegressor(
    max_depth=5,
    min_samples_split=10,
    min_samples_leaf=5,
    random_state=42
)

tree.fit(X_train, y_train)
tree.predict(X_test)
y_pred = tree.predict(X_test)

r2 = r2_score(y_test, y_pred)
print(r2 )

from xgboost import XGBRegressor
xgb_model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

# Train the model
xgb_model.fit(X_train, y_train)

# Prediction
y_pred_xgb = xgb_model.predict(X_test)

# R²
r2_xgb = r2_score(y_test, y_pred_xgb)
print(r2_xgb)

#Building ANN
ann=tf.keras.models.Sequential()
ann.add(tf.keras.layers.Dense(units=10,activation='relu'))#10 neurons in the first hidden layer
ann.add(tf.keras.layers.Dense(units=10,activation='relu'))#10 neurons in second hidden layer
ann.add(tf.keras.layers.Dense(units=1))
ann.compile(optimizer='adam',loss='mean_squared_error')
ann.fit(X_train,y_train,batch_size=32,epochs=100)

y_pred=ann.predict(X_test)
np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1)
print(r2_score(y_test,y_pred))
