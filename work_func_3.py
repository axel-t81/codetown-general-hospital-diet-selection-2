## UP TO HERE: NEED TO STUDY (a) Dictionaries (b) Functions

patient_req_protein = 37.5
patient_req_carbohydrates = 45.0
patient_req_fat = 30.88

normal_diet = {
    "protein": 32.5,
    "carbohydrates": 60.0,
    "fat": 40.86
}

oncology_diet = {
    "protein": 35.0,
    "carbohydrates": 52.5,
    "fat": 37.63
}

cardiology_diet = {
    "protein": 32.5,
    "carbohydrates": 30.0,
    "fat": 26.88
}

diabetes_diet = {
    "protein": 20.0,
    "carbohydrates": 27.5,
    "fat": 27.95
}

kidney_diet = {
    "protein": 15.0,
    "carbohydrates": 55.0,
    "fat": 23.65
}

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
    return total_error

def choose_diet(protein, carbohydrates, fat):
    patient_diet = {
        "protein": protein,
        "carbohydrates" : carbohydrates,
        "fat": fat
        }
    error_dict = {}
    error_dict["Normal"] = calculate_error(normal_diet, patient_diet)
    error_dict["Oncology"] = calculate_error(oncology_diet, patient_diet)
    error_dict["Cardilogy"] = calculate_error(cardiology_diet, patient_diet)
    error_dict["Diabetes"] = calculate_error(diabetes_diet, patient_diet)
    error_dict["Kidney"] = calculate_error(kidney_diet, patient_diet)
    print(error_dict)

    temp = min(error_dict.values())
    print(temp)

    key_list = list(error_dict.keys())
    val_list = list(error_dict.values())
    lowest_error_diet = val_list.index(temp)
    print(key_list[lowest_error_diet])

    return lowest_error_diet


choose_diet(patient_req_protein, patient_req_carbohydrates, patient_req_fat)