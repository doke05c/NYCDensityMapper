import json
from pprint import pprint

with open('sample_UWS.geojson') as f:
    data = json.load(f)

    sumarea = 0
    for i in data['features']:
        area = i['properties']['lotarea']
        sumarea += area
    print("This block has", sumarea, "sq. feet of lot area.")