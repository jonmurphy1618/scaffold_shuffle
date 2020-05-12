#!/usr/bin/env python

from sodapy import Socrata


client = Socrata("data.cityofnewyork.us", None)
db_id = "ipu4-2q9a"

def pull_dob_data( limit = 1):
	borough = "MANHATTAN"
	street_name = "CANAL STREET"

	return client.get(db_id, \
			limit = limit, \
			borough=borough, \
			street_name=street_name, \
			select="house__, \
				street_name, \
				zip_code, \
				bldg_type, \
				work_type, \
				permit_status, \
				filing_status, \
				permit_type, \
				permit_sequence__, \
				permit_subtype, \
				filing_date, \
				issuance_date, \
				expiration_date, \
				job_start_date, \
				dobrundate, \
				permit_si_no, \
				gis_latitude, \
				gis_longitude, \
				gis_council_district, \
				gis_census_tract, \
				gis_nta_name")

print(pull_dob_data(limit = 1))
