import json
from pprint import pprint
from matplotlib import pyplot as plt
import math
import gc

#the more dense the housing, the brighter the wavelength color the block is. 
#this scales linearly up to 1000+ units/acre
def draw_red(density):
    if (density >= 0 and density <= 80):
        return 1
    elif (density > 80 and density <= 160):
        return (2-(0.0125)*density)
    elif (density > 160 and density <= 240):
        return 0
    elif (density > 240 and density <= 320):
        return ((0.0125)*density-3)
    elif (density > 320):
        return 1

def draw_green(density):
    if (density >= 0 and density <= 80):
        return (0.0125*density)
    elif (density > 80 and density <= 160):
        return 1
    elif (density > 160 and density <= 240):
        return (3-(0.0125)*density)
    elif (density > 240 and density <= 320):
        return 0
    elif (density > 320 and density <= 400):
        return (0.00625)*density-2
    else:
        return 0.75

def draw_blue(density):
    if (density >= 0 and density <= 160):
        return 0
    elif (density > 160 and density <= 240):
        return ((0.0125)*density-2)
    elif (density > 240):
        return 1

# for i in range (0,501):
#     print(draw_red(i), draw_green(i), draw_blue(i))

qns_super_dict = {}#queens-super-dictionary

#helps the super-dictionary organize the block data
def dict_block_checker(dict, block):
    if block not in dict:
        dict[block] = {
        "sum_area_sqft": 0,
        "sum_units_res": 0,
        "coords_list": [],
        "density_acre": 0
        }



with open('../data/4-data.json') as f:
    data = json.load(f)

    for i in data['features']:

        #check if block exists, make new dict entry if not
        dict_block_checker(qns_super_dict, i['properties']['block'])

        #add to block area
        qns_super_dict[i['properties']['block']]["sum_area_sqft"] += i['properties']['lotarea']
        
        #add to block res unit count
        qns_super_dict[i['properties']['block']]["sum_units_res"] += i['properties']['unitsres'] 

        #add to coordinate list
        qns_super_dict[i['properties']['block']]["coords_list"].append(i['geometry']['coordinates'][0][0])

    #in a loop, calculate density by block in the super-dict
    for i in qns_super_dict.values():
        if (i["sum_units_res"] > 0):
            i["density_acre"] = i["sum_units_res"] / (i["sum_area_sqft"] / 43560)

    plt.figure()
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')

    #in a loop, render each block
    for i in qns_super_dict.values():
        # print(i["density_acre"])    
        for j in i["coords_list"]:
            xs, ys = zip(*j)
            if i["density_acre"] > 1:
                # if (draw_red(i["density_acre"]) < 0 or draw_red(i["density_acre"]) > 1 or draw_green(i["density_acre"]) < 0 or draw_green(i["density_acre"]) > 1 or draw_blue(i["density_acre"]) < 0 or draw_blue(i["density_acre"])) > 1:
                #     print(i["density_acre"])
                plt.fill(xs,ys, color=(draw_red(i["density_acre"]), draw_green(i["density_acre"]), draw_blue(i["density_acre"])))
            else: 
                plt.fill(xs,ys, color=(0,0,0))
    del f
    gc.collect

del qns_super_dict
gc.collect

plt.subplots_adjust(left=None, bottom=0.028, right=None, top=1, wspace=None, hspace=None)
plt.show()

# plt.savefig("../densitymap.png", dpi='figure', format=None, metadata=None,
#         bbox_inches=None, pad_inches=0.1,
#         facecolor='auto', edgecolor='auto',
#         backend=None)
