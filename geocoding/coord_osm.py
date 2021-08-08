#%%
import pandas as pd
from tqdm import tqdm
from pathlib import Path

from geocoding.nomi_example import osm

#%%

root = Path(__file__).parent.parent
df = pd.read_csv(root / "_towns.csv")

# FIMXE: если известен region_name_ao - используем его вместо region_name
#        для запроса к OSM.
# FIMXE: если в названии города есть "ё" в alt_city_name.json -
#        используем название города с "ё".


def iterate(df, n=0):
    gen = df[["city", "region_name"]]
    if n:
        gen = gen.sample(n)
    for _, (city, region_name) in tqdm(gen.iterrows()):
        yield city, region_name


out = []
n = 0
for city, region_name in iterate(df, n):
    print(city, region_name)
    resp = osm(city, region_name)
    resp["query_city"] = city
    resp["query_region"] = region_name
    print(resp)
    out.append(resp)

of = pd.DataFrame(out)
if n == 0:
    of.to_csv("coord_osm.csv")
