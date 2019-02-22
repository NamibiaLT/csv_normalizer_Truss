import csv_normalizer as csvn

sample_file = 'sample.csv'
broken_sample_file = 'sample-with-broken-utf8.csv'
zipcode = 1
fullname = 'Monkey Alberto'
timestamp = '10/20/19 1:00:00 AM'
address = "100 Hoover Dr., Sampletown, NH"
no_commas_address = "Hey there this is a town"

def test_read_stdin_as_dataframe():
	assert csvn.read_stdin_as_dataframe() == data_frame

def test_parse_timestamp():
		assert csvn.parse_timestamp(timestamp) == '2019-10-20T04:00:00-04:00'

def test_format_zipcodes():
	assert csvn.format_zipcodes(zipcode) == '00001'

def test_convert_names_colmn_to_uppercase():
	assert csvn.convert_names_colmn_to_uppercase(fullname) == 'MONKEY ALBERTO'

def test_parse_address():
	assert csvn.parse_address(address) == "100 Hoover Dr., Sampletown, NH"
	assert csvn.parse_address(no_commas_address) == "Hey there this is a town"
