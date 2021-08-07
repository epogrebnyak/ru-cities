import pandas as pd
from math import radians, cos, sin, asin, sqrt
import time

start_time = time.time()

def haversine(lon1, lat1, lon2, lat2):

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6371* c
    return km

df1 = pd.DataFrame(data=pd.read_csv("../assets/towns.csv"), columns=['city',"region_name",'lat', 'lon'])
df2 = pd.DataFrame(data=pd.read_csv("../geocoding/coord_osm.csv"),columns=['query_city',"query_region",'lat', 'lon'])
df2 = df2.rename(columns={'query_city': 'city', "query_region" : "region_name"})

df3 = df1.merge(df2[['city', 'lat', 'lon']], how='outer', on='city')

df3['distance_km'] = df3.apply(lambda row: haversine(row['lon_x'],row['lat_x'],row['lon_y'],row['lat_y']), axis=1)

df4 = pd.DataFrame(df3, columns=['lon_x', 'lat_x','lon_y',"lat_y"])

df3 = df3.sort_values(by=['distance_km'],ascending=False)

csv = pd.DataFrame(df3)
csv.to_csv("coord_compare.csv")

print("Finished! Time: " + str(round(time.time() - start_time, 2)) + "s")