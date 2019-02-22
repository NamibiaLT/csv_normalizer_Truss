import pandas as pd
import datetime
import time
import pytz


a_file = 'sample.csv'

def open_and_read_csv(a_file):
	data_frame = pd.read_csv(a_file, sep= ',', na_values=['None', 'none'])

	return data_frame

data_frame = open_and_read_csv(a_file)

def parse_datetime(data_frame):
	'''
	Format timestamp column to ISO-8601 and
	convert timestamp to US/Eastern
	'''

	datetime_obj_naive = pd.to_datetime(data_frame['Timestamp'],errors='coerce')

	datetime_obj_eastern = pytz.timezone('US/Eastern').localize(datetime_obj_naive)
	# iso_formatted_eastern = datetime_obj_eastern.isoformat()



# open_and_read_csv('sample.csv')
# format_zipcodes(data_frame)
# convert_names_colmn_to_uppercase(data_frame)
# # parse_datetime(data_frame)

