import pandas
import matplotlib

#saving the data file as a variable
filename = "clean_usgs_data.txt"

#loading the data file into pandas
database = pandas.read_csv(filename, sep='\t')
#print(database)

##renaming the columns to make more human readable
database = database.rename(columns={"75905_00065_30800": "gauge_height", "75906_00060_00003": "discharge"})
#print(database)

#deleting some unnecessary rows and columns
database = database.drop(['75905_00065_30800_cd', '75906_00060_00003_cd', 'agency_cd', 'site_no'], axis=1)
database = database.drop([0], axis=0)
#print(database)


