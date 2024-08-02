import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, area_type, sqft, bath, balcony, bed):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    try: 
        area_index = __data_columns.index(area_type.lower())
    except:
        area_index = -1
    
    arr = np.zeros(len(__data_columns))
    arr[0] = sqft
    arr[1] = bath
    arr[2] = balcony
    arr[3] = bed
    if (loc_index >= 0) and (area_index >= 0):
        arr[loc_index] = 1
    
    return round(__model.predict([arr])[0], 2)
    

def get_location_names():
    return __locations


def load_saved_artifacts():
    print ("loading saved artifacts... start")
    
    global __data_columns
    global __locations
    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:245]
        
    global __model
    with open("./artifacts/Bengaluru_house_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
        print("loading saved artifacts... done")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 'Super built-up  Area', 1000, 3, 2, 3))
    print(get_estimated_price('1st Phase JP Nagar', 'Built-up  Area', 1000, 2, 1, 2))
    print(get_estimated_price('Kalhalli', 'Built-up  Area', 1000, 2, 1, 2))
    print(get_estimated_price('Ejipura', 'Plot  Area', 1000, 2, 2, 2))