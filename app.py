#!/usr/bin/env python

from sodapy import Socrata

client = Socrata("data.cityofnewyork.us", None)

results = client.get("ipu4-2q9a", limit=1)
print(results)
#with open('test.output', 'w') as file:
#    file.write(results)
#file.closed
