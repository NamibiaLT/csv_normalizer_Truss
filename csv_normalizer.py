import pandas as pd
from datetime import datetime
from pytz import timezone
import io
import sys


a_file = 'sample.csv'

def read_stdin_as_dataframe():
	'''
	Invalid characters will be replaced with the Unicode Replacement
	Character.
	If that replacement makes data invalid (for example,
	because it turns a date field into something unparseable),
	a warning will be printed to `stderr`
	and the row will be dropped from output

	Pandas is used because it handles address commas
	'''
	raw_data = sys.stdin.detach().read()
	decoded_data = raw_data.decode('utf-8', 'replace')
	data_frame = pd.read_csv(io.StringIO(decoded_data), encoding='utf-8')

	return data_frame

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

