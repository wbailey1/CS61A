def make_city(name, lat, lon):
    return [name, lat, lon]

def get_name(city):
    return city[0]

def get_lat(city):
    return city[1]

def get_lon(city):
    return city[2]

from math import sqrt
def distance(city_1, city_2):
    lat_1, lon_1 = get_lat(city_1), get_lon(city_1)
    lat_2, lon_2 = get_lat(city_2), get_lon(city_2)
    return sqrt((lat_1 - lat_2)**2 + (lon_1 - lon_2)**2)
