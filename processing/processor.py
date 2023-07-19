import json
from pprint import pprint
from matplotlib import pyplot as plt
import math

#the more dense the housing, the greener the block is. 
#this scales logarithmically up to 1000 units/acre
def density_to_color(density):
    if density < 1:
        return 0
    elif density < 999:
        return math.log(density,10)/3
    else:
        return 1

mnh_super_dict = {}#manhattan-super-dictionary
bx_super_dict = {}#bronx-super-dictionary
bk_super_dict = {}#brooklyn-super-dictionary
qns_super_dict = {}#queens-super-dictionary
si_super_dict = {}#staten-island-super-dictionary

#helps the super-dictionary organize the block data
def dict_block_checker(dict, block):
    if block not in dict:
        dict[block] = {
        "sum_area_sqft": 0,
        "sum_units_res": 0,
        "coords_list": [],
        "density_acre": 0
        }



with open('1-data.json') as f:
    data = json.load(f)

    for i in data['features']:

        #check if block exists, make new dict entry if not
        dict_block_checker(mnh_super_dict, i['properties']['block'])

        #add to block area
        mnh_super_dict[i['properties']['block']]["sum_area_sqft"] += i['properties']['lotarea']
        
        #add to block res unit count
        mnh_super_dict[i['properties']['block']]["sum_units_res"] += i['properties']['unitsres'] 

        #add to coordinate list
        mnh_super_dict[i['properties']['block']]["coords_list"].append(i['geometry']['coordinates'][0][0])

    #in a loop, calculate density by block in the super-dict
    for i in mnh_super_dict.values():
        i["density_acre"] = i["sum_units_res"] / (i["sum_area_sqft"] / 43560)

    plt.figure()
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')

    #in a loop, render each block
    for i in mnh_super_dict.values():
        # print(i["density_acre"])    
        for j in i["coords_list"]:
            xs, ys = zip(*j)
            if i["density_acre"] > 0.1:
                plt.fill(xs,ys, color=(1-(density_to_color(i["density_acre"])), density_to_color(i["density_acre"]), 0))

with open('2-data.json') as f:
    data = json.load(f)

    for i in data['features']:

        #check if block exists, make new dict entry if not
        dict_block_checker(bx_super_dict, i['properties']['block'])

        #add to block area
        bx_super_dict[i['properties']['block']]["sum_area_sqft"] += i['properties']['lotarea']
        
        #add to block res unit count
        bx_super_dict[i['properties']['block']]["sum_units_res"] += i['properties']['unitsres'] 

        #add to coordinate list
        bx_super_dict[i['properties']['block']]["coords_list"].append(i['geometry']['coordinates'][0][0])

    #in a loop, calculate density by block in the super-dict
    for i in bx_super_dict.values():
        if i["sum_area_sqft"] > 0:
            i["density_acre"] = i["sum_units_res"] / (i["sum_area_sqft"] / 43560)

    #in a loop, render each block
    for i in bx_super_dict.values():
        # print(i["density_acre"])    
        for j in i["coords_list"]:
            xs, ys = zip(*j)
            if i["density_acre"] > 0.2:
                plt.fill(xs,ys, color=(1-(density_to_color(i["density_acre"])), density_to_color(i["density_acre"]), 0))

with open('3-data.json') as f:
    data = json.load(f)

    for i in data['features']:

        #check if block exists, make new dict entry if not
        dict_block_checker(bk_super_dict, i['properties']['block'])

        #add to block area
        bk_super_dict[i['properties']['block']]["sum_area_sqft"] += i['properties']['lotarea']
        
        #add to block res unit count
        bk_super_dict[i['properties']['block']]["sum_units_res"] += i['properties']['unitsres'] 

        #add to coordinate list
        bk_super_dict[i['properties']['block']]["coords_list"].append(i['geometry']['coordinates'][0][0])

    #in a loop, calculate density by block in the super-dict
    for i in bk_super_dict.values():
        if i["sum_area_sqft"] > 0:
            i["density_acre"] = i["sum_units_res"] / (i["sum_area_sqft"] / 43560)

    #in a loop, render each block
    for i in bk_super_dict.values():
        # print(i["density_acre"])    
        for j in i["coords_list"]:
            xs, ys = zip(*j)
            if i["density_acre"] > 0.2:
                plt.fill(xs,ys, color=(1-(density_to_color(i["density_acre"])), density_to_color(i["density_acre"]), 0))

with open('4-data.json') as f:
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
        if i["sum_area_sqft"] > 0:
            i["density_acre"] = i["sum_units_res"] / (i["sum_area_sqft"] / 43560)

    #in a loop, render each block
    for i in qns_super_dict.values():
        # print(i["density_acre"])    
        for j in i["coords_list"]:
            xs, ys = zip(*j)
            if i["density_acre"] > 0.2:
                plt.fill(xs,ys, color=(1-(density_to_color(i["density_acre"])), density_to_color(i["density_acre"]), 0))

with open('5-data.json') as f:
    data = json.load(f)

    for i in data['features']:

        #check if block exists, make new dict entry if not
        dict_block_checker(si_super_dict, i['properties']['block'])

        #add to block area
        si_super_dict[i['properties']['block']]["sum_area_sqft"] += i['properties']['lotarea']
        
        #add to block res unit count
        si_super_dict[i['properties']['block']]["sum_units_res"] += i['properties']['unitsres'] 

        #add to coordinate list
        si_super_dict[i['properties']['block']]["coords_list"].append(i['geometry']['coordinates'][0][0])

    #in a loop, calculate density by block in the super-dict
    for i in si_super_dict.values():
        if i["sum_area_sqft"] > 0:
            i["density_acre"] = i["sum_units_res"] / (i["sum_area_sqft"] / 43560)

    #in a loop, render each block
    for i in si_super_dict.values():
        # print(i["density_acre"])    
        for j in i["coords_list"]:
            xs, ys = zip(*j)
            if i["density_acre"] > 0.2:
                plt.fill(xs,ys, color=(1-(density_to_color(i["density_acre"])), density_to_color(i["density_acre"]), 0))

    plt.show()

