# -*- coding: utf-8 -*-

import pandas as pd

import statsmodels.api as sm

import numpy as np

# Data Prepration
wage_data = pd.read_csv("wage2.csv", header=None)

column_names = ["wage", "hours", "IQ", "KWW", "educ", "exper", "tenure", "age", "married", "black", "south", "urban", "sibs", "brthord", "meduc", "feduc", "lwage"]

wage_data.columns = column_names

# Model
y_model = np.log(wage_data['wage']) 
X_model = wage_data[['educ', 'exper', 'tenure']]

X_model = sm.add_constant(X_model) 

model_psoda = sm.OLS(y_model, X_model).fit() 
print(model_psoda.summary())
