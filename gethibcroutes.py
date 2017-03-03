#!/usr/bin/env python

import os
import json
import requests

response = requests.get("https://ridewithgps.com/groups/Histon-Impington-Bicycle-Club/routes.json?offset=0&limit=500")

routes = response.json()
print "Found %d routes" % len(routes)

for r in routes:
    distance_miles = r['distance'] * 0.000621371
    print "RouteID %d Desc %s Distance %.2f" % (r['id'], r['description'], distance_miles)
	
    file = str(r['id']) + ".json"
    url = "https://ridewithgps.com/routes/" + str(r['id']) + ".json"
    r = requests.get(url)
    with open(file, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)
