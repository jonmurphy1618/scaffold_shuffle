#!/usr/bin/env python

from sodapy import Socrata
from geojson import Point, Feature, FeatureCollection, dumps, MultiPoint

client = Socrata("data.cityofnewyork.us", "5kfMUjusxqGpjSi5EZtT2femX")
db_id = "ipu4-2q9a"
todays_date = "2020-01-01"

def pull_dob_data(limit = 1):
	borough = "MANHATTAN"
	# permit_type options: https://www1.nyc.gov/site/buildings/industry/permit-type-and-job-status-codes.page
	permit_type = "DM, FN, SH, SF, OT, FO, EA, NB, SG, EQ"

	# SQL query based on below site:
	# https://data.cityofnewyork.us/Housing-Development/DOB-Permit-Issuance/ipu4-2q9a
	return client.get(db_id,  query=f" \
		SELECT job__, gis_latitude, gis_longitude \
		WHERE borough='MANHATTAN' \
		AND expiration_date > {todays_date} \
		AND (permit_type='DM' \
		OR permit_type='FN' \
		OR permit_type='SH' \
		OR permit_type='SF' \
		OR permit_type='OT' \
		OR permit_type='FO' \
		OR permit_type='EA' \
		OR permit_type='NB' \
		OR permit_type='SG' \
		OR permit_type='EQ' \
		)\
		LIMIT {limit}")


def csv_output(limit = 1):
	with open('output_data.csv', 'w') as file:
		map_data = pull_dob_data(limit)
		for each in map_data:
			if each.get('gis_latitude') and each.get('gis_longitude'):
				file.writelines(f"{each['job__']},{each['gis_latitude']},{each['gis_longitude']}" + '\n')

def geojson_output(limit = 1):
	all_points = []
	with open('output_data.json', 'w') as file:
		map_data = pull_dob_data(limit)
		for each in map_data:
			if each.get('gis_latitude') and each.get('gis_longitude'):
				each_point = (float(each['gis_longitude']),float(each['gis_latitude']))
				all_points.append(each_point)
		file.writelines(dumps(FeatureCollection([Feature(geometry=MultiPoint(all_points))])))
#				each_point = Point((float(each['gis_latitude']),float(each['gis_longitude'])))
#				file.writelines(dumps(each_point))

def main():
#	pull_dob_data()
#	csv_output(limit = 1000)
	geojson_output(limit = 1000000)

main()
