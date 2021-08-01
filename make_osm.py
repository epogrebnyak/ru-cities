
#%%
from geocoding.nomi_example import osm
from tqdm import tqdm
import pandas as pd

#%%
df = pd.read_csv("towns.csv")

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