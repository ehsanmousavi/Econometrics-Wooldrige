# -*- coding: utf-8 -*-

import pandas as pd

import statsmodels.api as sm

import numpy as np

# Data Prepration
discrim_data = pd.read_csv("discrim.csv", header=None)

column_names = ["psoda", "pfries", "pentree", "wagest", "nmgrs", "nregs", "hrsopen", "emp", "psoda2", "pfries2", "pentree2", "wagest2", "nmgrs2", "nregs2", "hrsopen2", "emp2", "compown", "chain", "density", "crmrte", "state", "prpblck", "prppov", "prpncar", "hseval", "nstores", "income", "county", "lpsoda", "lpfries", "lhseval", "lincome", "ldensity", "NJ", "BK", "KFC", "RR"]

discrim_data.columns = column_names

discrim_data = discrim_data.replace(".", np.nan) 

print(discrim_data)

if discrim_data.isnull().values.any():
    print("DataFrame contains NaN values.")
else:
    print("DataFrame does not contain NaN values.")

discrim_data_cleaned = discrim_data.dropna(subset=['prpblck', 'income', 'psoda'], how='any')

discrim_data_cleaned.loc[:, ['prpblck', 'income', 'psoda']] = discrim_data_cleaned[['prpblck', 'income', 'psoda']].astype(float)

# Mean & Standard Deviation
mean_prpblck = discrim_data_cleaned['prpblck'].mean() 
mean_income = discrim_data_cleaned['income'].mean()

sd_prpblck = discrim_data_cleaned['prpblck'].std() 
sd_income = discrim_data_cleaned['income'].std() 

# Fit the Model (ii)
y_model = discrim_data_cleaned['psoda']
X_model = discrim_data_cleaned[['prpblck', 'income']]

X_model = sm.add_constant(X_model) 

model_psoda = sm.OLS(y_model, X_model).fit() 
print(model_psoda.summary())

# Fit the Model (iii)
y_model_simple = discrim_data_cleaned['psoda']
X_model_simple = discrim_data_cleaned['prpblck']

X_model_simple = sm.add_constant(X_model_simple) 

model_psoda_simple = sm.OLS(y_model_simple, X_model_simple).fit()
print(model_psoda_simple.summary())