import csv_normalizer as csvn

sample_file = 'sample.csv'
broken_sample_file = 'sample-with-broken-utf8.csv'
zipcode = 1
fullname = 'Monkey Alberto'
timestamp = '10/20/19 1:00:00 AM'
address = "100 Hoover Dr., Sampletown, NH"
missing_commas_address = "Hey there this is a town"
notes = "I am the very model of a modern major general"
unicode_notes = "This is some Unicode right h�xxx ü ¡! 😀"
duration_string = "00:00:01.100"
second_duration_string = "00:00:10.100"

# def test_read_stdin_as_dataframe():
# 	assert csvn.read_stdin_as_dataframe() == data_frame

def test_parse_timestamp():
		assert csvn.parse_timestamp(timestamp) == '2019-10-20T04:00:00-04:00'

def test_format_zipcodes():
	assert csvn.format_zipcodes(zipcode) == '00001'

def test_convert_names_colmn_to_uppercase():
	assert csvn.convert_names_colmn_to_uppercase(fullname) == 'MONKEY ALBERTO'

def test_parse_address():
	assert csvn.parse_address(address) == '"100 Hoover Dr., Sampletown, NH"'
	assert csvn.parse_address(missing_commas_address) == "Hey there this is a town"

def test_parse_notes():
	assert csvn.parse_notes(notes) == "I am the very model of a modern major general"
	assert csvn.parse_notes(unicode_notes) == "This is some Unicode right h�xxx ü ¡! 😀"

def test_parse_duration():
	assert csvn.parse_duration(duration_string) == '1.100'

def test_parse_total_duration():
	assert csvn.parse_total_duration(duration_string, second_duration_string) == '11.200'
