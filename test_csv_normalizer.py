import csv_normalizer as csvn

sample_file = 'sample.csv'
broken_sample_file = 'sample-with-broken-utf8.csv'

def test_read_stdin_as_dataframe():
	assert csvn.read_stdin_as_dataframe(broken_sample_file) == data_frame

def test_parse_datetime():
		assert csvn.parse_datetime(sample_file) == data_frame['Timestamp']

def test_format_zipcodes():
	assert csvn.format_zipcodes(sample_file)[1] == '00001'

def test_convert_names_colmn_to_uppercase():
	assert csvn.convert_names_colmn_to_uppercase(sample_file)[0] == 'MONKEY ALBERTO'
