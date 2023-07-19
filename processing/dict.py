totaldict = {
    1525: {
        "sum_area_sqft": 0,
        "sum_units_res": 0,
        "coords_list": [],
        "density_acre": 0
    },
    1526: {
        "sum_area_sqft": 0,
        "sum_units_res": 0,
        "coords_list": [],
        "density_acre": 0
    }
}

def dict_block_checker(dict, block):
    if block not in dict:
        dict[block] = {
        "sum_area_sqft": 0,
        "sum_units_res": 0,
        "coords_list": [],
        "density_acre": 0
        }

dict_block_checker(totaldict, 1527)
totaldict[1527]["sum_area_sqft"] = 3
dict_block_checker(totaldict, 1527)
print(totaldict)