# Load Libraries
library(readr)

# Colnames
column_names_bwght <- c("faminc", "cigtax", "cigprice", "bwght", "fatheduc", "motheduc", "parity", "male", "white", "cigs", "lbwght", "bwghtlbs", "packs", "lfaminc")

# Import Data
bwght_data <- read.csv("bwght.csv", header = FALSE, col.names = column_names_bwght)

# Calculate the correlation between cigs and faminc
correlation_cigs_faminc <- cor(bwght_data$cigs, bwght_data$faminc)
print(correlation_cigs_faminc)

# The equation
model_without_faminc <- lm(bwght ~ cigs, data = bwght_data)
summary(model_without_faminc)

model_with_faminc <- lm(bwght ~ cigs + faminc, data = bwght_data)
summary(model_with_faminc)
