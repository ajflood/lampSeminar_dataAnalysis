import pandas
import numpy
import statsmodels.api as statsmodels
import statsmodels.formula.api as formulastats

# loading a data set from statsmodels for examples purposes
data = statsmodels.datasets.get_rdataset("Guerry", "HistData").data
print(data)

# Fit regression model (using the natural log of one of the regressors)
results = formulastats.ols('Lottery ~ Literacy + numpy.log(Pop1831)', data=data).fit()
print(results.summary())

# Fit a different regression model with interactions
results = formulastats.ols('Lottery ~ Lottery + Instruction + Lottery*Instruction', data=data).fit()
print(results.summary())

# Fit a different regression model with categorical variables
results = formulastats.ols('Lottery ~ Lottery + Instruction + C(Region)', data=data).fit()
print(results.summary())
