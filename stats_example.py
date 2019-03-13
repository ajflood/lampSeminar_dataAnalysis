import pandas
import statsmodels.api as statsmodels
import statsmodels.formula.api as formulastats

#loading a data set from statsmodels for examples purposes
data = statsmodels.datasets.get_rdataset("Guerry", "HistData").data
print(data)
