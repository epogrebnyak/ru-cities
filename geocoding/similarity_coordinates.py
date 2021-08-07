import pandas as pd

df1 = pd.DataFrame(data=pd.read_csv("../assets/towns.csv"), columns=['city','lat', 'lon'])
df2 = pd.DataFrame(data=pd.read_csv("../geocoding/coord_osm.csv"),columns=['query_city','lat', 'lon'])
df2 = df2.rename(columns={'query_city': 'city'})

df3 = df1.merge(df2[['city', 'lat', 'lon']], how='outer', on='city')


df3['compare_lat'] = df3['lat_x'] == df3['lat_y']
df3['compare_lon'] = df3['lon_x'] == df3['lon_y']

csv = pd.DataFrame(df3)
csv.to_csv("coord_compare.csv")
