#Load library
library(readr)

# Colnames
column_names_discrim <- c("psoda", "pfries", "pentree", "wagest", "nmgrs", "nregs", "hrsopen", "emp", "psoda2", "pfries2", "pentree2", "wagest2", "nmgrs2", "nregs2", "hrsopen2", "emp2", "compown", "chain", "density", "crmrte", "state", "prpblck", "prppov", "prpncar", "hseval", "nstores", "income", "county", "lpsoda", "lpfries", "lhseval", "lincome", "ldensity", "NJ", "BK", "KFC", "RR")

#Import Data
discrim_data <- read.csv("discrim.csv", header = FALSE, col.names = column_names_discrim)

#As Numeric
discrim_data$prpblck <- as.numeric(as.character(discrim_data$prpblck))
discrim_data$income <- as.numeric(as.character(discrim_data$income))
discrim_data$psoda <- as.numeric(as.character(discrim_data$psoda))

discrim_data <- na.omit(discrim_data)

#Mean & Standard Deviation
mean_prpblck <- mean(discrim_data$prpblck)
mean_income <- mean(discrim_data$income)

sd_prpblck <- sd(discrim_data$prpblck)
sd_income <- sd(discrim_data$income)

# Fit the Model (ii)
model_psoda <- lm(psoda ~ prpblck + income, data = discrim_data)

summary(model_psoda)

# Fit the Model (iii)
model_psoda_simple <- lm(psoda ~ prpblck , data = discrim_data)

summary(model_psoda_simple)
