# %%
import pandas as pd

df = pd.read_csv("towns.csv")
cf = pd.read_csv("coord_dadata.csv")
# %%


cols = ['city_x', 
'population', 
'geo_lat', 
'geo_lon', 
'region_name', 
'region_iso_code',
'federal_district', 
'capital_marker', 
]

cf[cf.city.str.contains("ё").fillna(False)].city

df.merge(cf, 
left_on=["city", "region_name"], 
right_on=["query_city", "query_region"])[cols]# %%
