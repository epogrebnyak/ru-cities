#%%
import pandas as pd
from tqdm import tqdm
from pathlib import Path
import json
from geocoding.nomi_example import osm

#%%
root = Path(__file__).parent.parent
df = pd.read_csv(root / "_towns.csv")

alt_cities = Path(root / "assets" / "alt_city_names.json").read_text(encoding="utf-8")
alt_cities = json.loads(alt_cities)


# FIMXE: [x] если известен region_name_ao - используем его вместо region_name
#        для запроса к OSM.
# FIMXE: [x] если в названии города есть "ё" в alt_city_name.json -
#        используем название города с "ё".

def check_city(city):
    if city in alt_cities:
        return alt_cities[city]
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

of = pd.DataFrame(out)
if n == 0:
    of.to_csv("coord_osm.csv")

