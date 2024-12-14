#Libraries
library(readr)

#COlumns
column_names_wage <- c("wage", "hours", "IQ", "KWW", "educ", "exper", "tenure", "age", "married", "black", "south", "urban", "sibs", "brthord", "meduc", "feduc", "lwage")

#Import data
wage_data <- read.csv("wage2.csv", header = FALSE, col.names = column_names_wage)

#Model

wage_model <- lm(log(wage) ~ educ + exper + tenure, data = wage_data)

summary(wage_model)
