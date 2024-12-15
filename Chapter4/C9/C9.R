#Libraries
library(readr)
library(dplyr)

# Colnames
column_names_discrim <- c("psoda", "pfries", "pentree", "wagest", "nmgrs", "nregs", "hrsopen", "emp", "psoda2", "pfries2", "pentree2", "wagest2", "nmgrs2", "nregs2", "hrsopen2", "emp2", "compown", "chain", "density", "crmrte", "state", "prpblck", "prppov", "prpncar", "hseval", "nstores", "income", "county", "lpsoda", "lpfries", "lhseval", "lincome", "ldensity", "NJ", "BK", "KFC", "RR")

# Import Data
discrim_data <- read.csv("discrim.csv", header = FALSE, col.names = column_names_discrim)

# Data preparation
discrim_data[discrim_data == "."] <- NA

discrim_data <- discrim_data %>% mutate(across(everything(), ~ as.numeric(.)))

# Model (i)
discrim_model_i <- lm(log(psoda) ~ prpblck + log(income) + prppov, data = discrim_data)

summary(discrim_model_i)

#Correlation
cor(log(discrim_data$income), discrim_data$prppov, use = "complete.obs")

# Model (iii)
discrim_model_iii <- lm(log(psoda) ~ prpblck + log(income) + prppov + log(hseval), data = discrim_data)

summary(discrim_model_iii)

cor(log(discrim_data$hseval), discrim_data$prppov, use = "complete.obs")
