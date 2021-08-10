#%%
import pandas as pd
from tqdm import tqdm
from pathlib import Path
import json
from geocoding.nomi_example import osm

#%%
root = Path(__file__).parent.parent
df = pd.read_csv(root / "_towns.csv")

# FIMXE: [x] если известен region_name_ao - используем его вместо region_name
#        для запроса к OSM.
# FIMXE: [x] если в названии города есть "ё" в alt_city_name.json -
#        используем название города с "ё".

with open( root / "assets" / "alt_city_names.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

def check_city(city):

    if city in data:
        return data[city]
    return city

def check_region(region_name,region_name_ao):
    try:
        float(region_name_ao)
        return region_name
    except ValueError:
        return region_name_ao


def iterate(df, n=0):
    gen = df[["city", "region_name", "region_name_ao"]]
    if n:
        gen = gen.sample(n)
    for _, (city, region_name,region_name_ao) in tqdm(gen.iterrows()):

        city = check_city(city)
        region_name = check_region(region_name,region_name_ao)

        yield city, region_name


out = []
n = 0
for city, region_name in iterate(df, n):
    print(city, region_name)
    resp = osm(city, region_name)
    resp["query_city"] = city
    resp["query_region"] = region_name
    out.append(resp)

f.close()

of = pd.DataFrame(out)
if n == 0:
    of.to_csv("coord_osm.csv")

