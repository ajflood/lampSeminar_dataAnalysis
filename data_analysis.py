import pandas
import matplotlib.pyplot as plt

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

#converting the data to numbers from strings
database["gauge_height"] = pandas.to_numeric(database["gauge_height"])
database["discharge"] = pandas.to_numeric(database["discharge"])
#print(database)

###showing some slicing and data selection
#gauge_height_slice = database['gauge_height']
##print(gauge_height_slice)
#multi_column_slice = database.loc[:, ['datetime', 'gauge_height']]
##print(multi_column_slice)

#specific_date_by_index = database.iloc[0]
##print(specific_date_by_index)
#specific_date_by_matching_date = database.loc[database['datetime'] == '2019-03-01']
##print(specific_date_by_matching_date)





