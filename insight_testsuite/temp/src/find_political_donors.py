from ByZip import ByZip
from ByDate import ByDate
from collections import namedtuple
import sys
import cProfile
import re
import datetime

input_file_path = sys.argv[1]
output_zip_path = sys.argv[2]
output_date_path = sys.argv[3]
zipValidator = re.compile("^[0-9]{5}$")

# Wrapper function where input textfile is read
# For (cmtd_id, zip), each line is written in the output file as each input line is read
# For (cmtd_id, date), each line is written after reading in the entire data
# I store each tuple pair (cmtd_id, zip), (cmtd_id, date) to its class object in a dictionary for efficient search

def process_data(input_file_path, output_zip_path, output_date_path):
	idZip = {}
	idDate = {}

	with open(output_zip_path, 'w') as w:
		with open(input_file_path, 'r') as f:
			for line in f:
				values = line.split('|')
				other = values[15]
				cmtd_id = values[0]
				trx_amt = values[14]
				if other or cmtd_id == '' or trx_amt == '': 								# if any of three values is empty, the data is invalid
					continue
				trx_amt = int(trx_amt)
				zipcode = values[10][0:5]
				date = values[13]

				if checkValidZip(zipcode):
					tup = (cmtd_id, zipcode)
					if tup in idZip:
						entry = idZip[tup]
					else:
						entry = ByZip(cmtd_id, zipcode)
						idZip[tup] = entry

					entry.increment(trx_amt)
					w.write(entry.toString())

				if checkValidDate(date):
					tup = (cmtd_id, date)
					if tup in idDate:
						entry = idDate[tup]
					else:
						entry = ByDate(cmtd_id, date)
						idDate[tup] = entry
					entry.increment(trx_amt)


	with open(output_date_path, 'w') as w_date:
		for each in sorted(idDate.keys(), key = lambda x: (x[0], x[1])):
			w_date.write(idDate[each].toString())

# Checks the validity of the zipcode, using regex
# The function assumes that any 5 digit combination is a valid zipcode

def checkValidZip(zipcode):
	result = zipValidator.match(zipcode)
	if result:
		return True
	return False

# Checks the validity of the date, using strptime
# But to enforce 'mmddyyyy', I explicity check for length as well

def checkValidDate(date):
	if len(date) < 8:
		return False
	try:
		datetime.datetime.strptime(date, '%m%d%Y')
		return True
	except ValueError:
		return False

if __name__ == '__main__':
	process_data(input_file_path, output_zip_path, output_date_path)

