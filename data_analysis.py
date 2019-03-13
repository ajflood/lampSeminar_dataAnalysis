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
database["datetime"] = pandas.to_datetime(database["datetime"])
#print(database)
#print(database.dtypes)

###showing some slicing and data selection
#gauge_height_slice = database['gauge_height']
##print(gauge_height_slice)
#multi_column_slice = database.loc[:, ['datetime', 'gauge_height']]
##print(multi_column_slice)

#specific_date_by_index = database.iloc[0]
##print(specific_date_by_index)
#specific_date_by_matching_date = database.loc[database['datetime'] == '2019-03-01']
##print(specific_date_by_matching_date)

###plotting examples
##histogram
#database.plot.hist(x='datetime', y='gauge_height')
#plt.savefig('histogram.png')
#plt.close('all')

##scatter
#plt.scatter(database['datetime'], database['discharge'])
#plt.savefig('scatter_plot.png')
#plt.close('all')

##line
#database.plot.line(x='datetime', y='discharge')
#plt.savefig('line_plot.png')
#plt.close('all')

##making a pretty plot
#ax1 = database.plot.line(x='datetime', y='gauge_height', c='r')
#ax2 = database.plot.line(x='datetime', y='discharge', c='b', secondary_y=True, ax=ax1)
#ax1.set_ylim([0., 20.])
#ax1.set_ylabel('The left y Axis')
#ax2.set_ylim(bottom=0.0)
#ax2.set_ylabel('The right y Axis')
#plt.title('Some title for your plot')
#plt.xlabel('The shared x Axis')
#plt.tight_layout()
#plt.savefig('pretty_plot.png')
#plt.close('all')


