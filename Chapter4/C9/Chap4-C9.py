# -*- coding: utf-8 -*-

import pandas as pd

import statsmodels.api as sm

import numpy as np


# Data Prepration
discrim_data = pd.read_csv("discrim.csv", header=None)

column_names = ["psoda", "pfries", "pentree", "wagest", "nmgrs", "nregs", "hrsopen", "emp", "psoda2", "pfries2", "pentree2", "wagest2", "nmgrs2", "nregs2", "hrsopen2", "emp2", "compown", "chain", "density", "crmrte", "state", "prpblck", "prppov", "prpncar", "hseval", "nstores", "income", "county", "lpsoda", "lpfries", "lhseval", "lincome", "ldensity", "NJ", "BK", "KFC", "RR"]

discrim_data.columns = column_names

discrim_data = discrim_data.replace(".", np.nan) 

discrim_data['psoda'] = pd.to_numeric(discrim_data['psoda'], errors='coerce')
discrim_data['income'] = pd.to_numeric(discrim_data['income'], errors='coerce')
discrim_data['prpblck'] = pd.to_numeric(discrim_data['prpblck'], errors='coerce')
discrim_data['prppov'] = pd.to_numeric(discrim_data['prppov'], errors='coerce')
discrim_data['hseval'] = pd.to_numeric(discrim_data['hseval'], errors='coerce')

if discrim_data.isnull().values.any():
    print("DataFrame contains NaN values.")
else:
    print("DataFrame does not contain NaN values.")
    
discrim_data_cleaned = discrim_data.dropna(subset=['prpblck', 'income', 'psoda', 'prppov'], how='any')

#Model (i)
y_model = np.log(discrim_data_cleaned['psoda']) 
X_model = discrim_data_cleaned[['prpblck', 'prppov']].copy() 
X_model.loc[:, 'log_income'] = np.log(discrim_data_cleaned['income'])

X_model = sm.add_constant(X_model) 

discrim_model_i = sm.OLS(y_model, X_model).fit() 
print(discrim_model_i.summary())

# Correlation income and prppov
discrim_data['log_income'] = np.log(discrim_data['income'])
correlation_income_prppov = discrim_data['log_income'].corr(discrim_data['prppov'])

# Model (iii)
discrim_data_cleaned = discrim_data_cleaned.dropna(subset=['hseval'], how='any')
y_model_iii = np.log(discrim_data_cleaned['psoda'])
X_model_iii = discrim_data_cleaned[['prpblck', 'prppov']].copy() 
X_model_iii.loc[:, 'log_income'] = np.log(discrim_data_cleaned['income'])
X_model_iii.loc[:, 'log_hseval'] = np.log(discrim_data_cleaned['hseval'])

X_model_iii = sm.add_constant(X_model_iii) 

discrim_model_iii = sm.OLS(y_model_iii, X_model_iii).fit() 
print(discrim_model_iii.summary())

# Correlation log(hseval) and prppove
discrim_data['log_hseval'] = np.log(discrim_data['hseval'])
correlation_log_hseval_prppov = discrim_data['log_hseval'].corr(discrim_data['prppov'])
