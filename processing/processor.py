import json
from pprint import pprint

with open('sample_UWS.geojson') as f:
    data = json.load(f)

    sumarea = 0
    sumunitsres = 0
    for i in data['features']:
        area = i['properties']['lotarea']
        unitsres = i['properties']['unitsres']
        sumarea += area
        sumunitsres += unitsres
    print("This block has", sumarea, "sq. feet of lot area.")
    print("This block has", sumunitsres, "residential units.")