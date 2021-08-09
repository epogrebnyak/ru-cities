#%%
import pandas as pd
from tqdm import tqdm
from pathlib import Path
import json
from ast import literal_eval
from geocoding.nomi_example import osm

#%%

# [x]FIMXE: если известен region_name_ao - используем его вместо region_name
#        для запроса к OSM.
# [x]FIMXE: если в названии города есть "ё" в alt_city_name.json -
#        используем название города с "ё".

root = Path(__file__).parent.parent
df = pd.read_csv(root / "_towns.csv")


with open( root / "assets" / "alt_city_names.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

def check_city(city):

    j = json.dumps(data,
               ensure_ascii=False,
               separators=(',', ': '))

    d = literal_eval(j)

    if city in d:
        return d[city]
    return city


def check_region(region_name_ao):
    try:
        float(region_name_ao)
        return False
    except ValueError:
        return True


def iterate(df, n=0):
    gen = df[["city", "region_name", "region_name_ao"]]

    for _, (city, region_name,region_name_ao) in tqdm(gen.iterrows()):

        if check_region(region_name_ao):
            x_region_name_ao = region_name_ao
        else:
            x_region_name_ao = ""

        x_city = check_city(city)

        yield x_city, region_name,x_region_name_ao


out = []
n = 0

for city, region_name, region_name_ao in iterate(df, n):
    resp = osm(city, region_name, region_name_ao)
    resp["query_city"] = city
    resp["query_region"] = region_name
    resp["query_region_ao"] = region_name_ao
    out.append(resp)

of = pd.DataFrame(out)
if n == 0:
    of.to_csv("coord_osm.csv")

f.close()