import json
from pprint import pprint
from matplotlib import pyplot as plt
import math

#the more dense the housing, the greener the block is. 
#this scales logarithmically up to 1000 units/acre
def density_to_color(density):
    return math.log(density,10)/3

with open('sample_village.geojson') as f:
    data = json.load(f)

    sum_area_sqft = 0
    sum_units_res = 0
    coords_list = []
    for i in data['features']:
        area = i['properties']['lotarea']
        units_res = i['properties']['unitsres']
        coord = i['geometry']['coordinates'][0][0]
        sum_area_sqft += area
        sum_units_res += units_res
        coords_list.append(coord)

    print("This block has", sum_area_sqft, "sq. feet of lot area.")
    print("This block has", sum_units_res, "residential units.")

    sum_area_acre = sum_area_sqft / 43560
    density_acre = sum_units_res / sum_area_acre

    print("This block's residential density is", round(density_acre, 2), "units per acre.")

    print(f"There are {len(coords_list)} buildings.")
    with open("save_coords_list.json", "w") as save_file:
        json.dump(coords_list, save_file, indent=2)

    plt.figure()
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    for i in coords_list:
        xs, ys = zip(*i)

        # plt.plot(xs,ys, color=(1-(density_to_color(density_acre)), density_to_color(density_acre), 0)) 
        if sum_units_res > 0:
            plt.fill(xs,ys, color=(1-(density_to_color(density_acre)), density_to_color(density_acre), 0))
    
    if sum_units_res == 0:
        print("Since this block has no residential units, it will be left out of the map.")
    
    plt.show()

