# Truss Software Engineering Interview
## Submission by: Namibia Torres
## The CSV Normalizer App:

This app is a tool that reads a CSV formatted file on `stdin` and
emits a normalized CSV formatted file on `stdout`. Normalized, in this
case, means:

* The entire CSV is in the UTF-8 character set.
* The Timestamp column should be formatted in ISO-8601 format.
* The Timestamp column should be assumed to be in US/Pacific time;
  please convert it to US/Eastern.
* All ZIP codes should be formatted as 5 digits. If there are less
  than 5 digits, assume 0 as the prefix.
* All name columns should be converted to uppercase. There will be
  non-English names.
* The Address column should be passed through as is, except for
  Unicode validation. Please note there are commas in the Address
  field; your CSV parsing will need to take that into account. Commas
  will only be present inside a quoted string.
* The columns `FooDuration` and `BarDuration` are in HH:MM:SS.MS
  format (where MS is milliseconds); please convert them to a floating
  point seconds format.
* The column "TotalDuration" is filled with garbage data. For each
  row, please replace the value of TotalDuration with the sum of
  FooDuration and BarDuration.
* The column "Notes" is free form text input by end-users; please do
  not perform any transformations on this column. If there are invalid
  UTF-8 characters, please replace them with the Unicode Replacement
  Character.

### Assumptions and More:
You can assume that the input document is in UTF-8 and that any times
that are missing timezone information are in US/Pacific. If a
character is invalid, please replace it with the Unicode Replacement
Character. If that replacement makes data invalid (for example,
because it turns a date field into something unparseable), print a
warning to `stderr` and drop the row from your output.

You can assume that the sample data we provide will contain all date
and time format variants you will need to handle.

## Python Version:
I am using Python 3.7

## Requirements:
To install the right versions of packages, you can do this in one go by typing the following in your terminal:
`pip install -r requirements.txt`

## Testing
The Pytest framework was used for testing. To install pytest and run the test file. First run:
`pip install pytest`
Then type the following command in your terminal:
`pytest test_csv_normalizer.py -v`

## Run app in terminal:
#### To run the app in your terminal, type the following command:
`cat [name_of_your_csv_fil.csv] | python3 csv_normalizer.py `
The command will look something like this in your terminal:
`cat sample-with-broken-utf8.csv | python3 csv_normalizer.py`

### Note:
* This code is meant to run on macOS 10.13
* Areas to complete: fix two broken tests
* Duration of test: 4 hours


