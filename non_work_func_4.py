## OKAY THIS WORKS!
## YOU HAVE NOW CUT & PASTE THE APPLICABLE FUNCTION CODE TO MEALS.PY
## BUT YOU WON'T DELETE THIS UNTIL YOUR COMFORTABLE IT CAN BE DELETED.
def calculate_error(diet, requirements):
    pro_diet = diet["protein"]
    pro_req = requirements["protein"]
    pro_error = abs(pro_diet - pro_req)

    carb_diet = diet["carbohydrates"]
    carb_req = requirements["carbohydrates"]
    carb_error = abs(carb_diet - carb_req)

    fat_diet = diet["fat"]
    fat_req = requirements["fat"]
    fat_error = abs(fat_diet - fat_req)

    total_error = (pro_error + carb_error + fat_error)
    print(total_error)



test_dict = {
    "protein": 16.0,
    "carbohydrates": 50.0,
    "fat": 23.00
}

kidney_dict = {
    "protein": 15.0,
    "carbohydrates": 55.0,
    "fat": 23.65
}

calculate_error(kidney_dict, test_dict)