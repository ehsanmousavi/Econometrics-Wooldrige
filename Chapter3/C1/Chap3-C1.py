# -*- coding: utf-8 -*-

import pandas as pd

import statsmodels.api as sm

# Data Prepration
bwght_data = pd.read_csv("bwght.csv", header=None)

column_names = ["faminc", "cigtax", "cigprice", "bwght", "fatheduc", "motheduc", "parity", "male", "white", "cigs", "lbwght", "bwghtlbs", "packs", "lfaminc"]

bwght_data.columns = column_names 

# Correlation cigs and faminc
correlation_cigs_faminc = bwght_data['cigs'].corr(bwght_data['faminc']) 

# Models
y = bwght_data['bwght']
X = bwght_data['cigs']

X = sm.add_constant(X) 

model_without_faminc = sm.OLS(y, X).fit()
print(model_without_faminc.summary())

y_with_faminc = bwght_data['bwght']
X_with_faminc = bwght_data[['cigs', 'faminc']]

X_with_faminc = sm.add_constant(X_with_faminc) 

model_with_faminc = sm.OLS(y_with_faminc, X_with_faminc).fit()
print(model_with_faminc.summary())
