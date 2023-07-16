import json
from pprint import pprint

with open('sample_UWS.geojson') as f:
    data = json.load(f)

    sum_area_sqft = 0
    sum_units_res = 0
    for i in data['features']:
        area = i['properties']['lotarea']
        units_res = i['properties']['unitsres']
        sum_area_sqft += area
        sum_units_res += units_res
    print("This block has", sum_area_sqft, "sq. feet of lot area.")
    print("This block has", sum_units_res, "residential units.")

    sum_area_acre = sum_area_sqft / 43560
    density_acre = sum_units_res / sum_area_acre

    print("This block's residential density is", round(density_acre, 2), "units per acre.")
