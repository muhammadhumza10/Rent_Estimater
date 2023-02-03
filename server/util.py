import pickle
import json
import numpy as np


__locations = None
__city = None
__data_columns = None
__model = None

def get_estimated_price(city,location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
        city_index = __data_columns.index(city.lower())
    except:
        loc_index = -1
        city_index = -1

    x = np.zeros(len(__data_columns))
    x1 = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1
    if city_index>=0:
        x[city_index] = 1

    return round(__model.predict([x,x1])[0]/10000,2)




def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations
    global __city

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:-5]  # first 3 columns are sqft, bath, bhk
        __city = __data_columns[-5:]

    global __model
    if __model is None:
        with open('./artifacts/Property_with_Feature_Engineering_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_city_names():
    return __city

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_city_names())
    print(get_estimated_price('Lahore','Punjab Govt Employees Society',1000, 3, 3))# other location
    print(get_estimated_price('Karachi','Shah Faisal Town',1000, 2, 2))# other location
    print(get_estimated_price('Karachi','Gulshan-e-Iqbal Town',1000, 3, 3)) # other location
    print(get_estimated_price('Karachi','North Nazimabad',1000, 2, 3))  # other location