import pandas
import matplotlib

#saving the data file as a variable
filename = "clean_usgs_data.txt"

#loading the data file into pandas
database = pandas.read_csv(filename, sep='\t')

print(database)




