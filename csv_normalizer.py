import pandas as pd
import datetime
import time
import pytz


a_file = 'sample.csv'

def open_and_read_csv(a_file):
	data_frame = pd.read_csv(a_file, sep= ',', na_values=['None', 'none'])

	return data_frame

data_frame = open_and_read_csv(a_file)

