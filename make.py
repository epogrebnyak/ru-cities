"""Cоздать файл towns.csv"""
import pandas as pd
from krasnodar import docx_files, extract, n_cities, process, yield_full_population

# %%
# rar folder is populated with rar/get.sh
if False:
    full_pop = []
    for path in docx_files("rar"):
        text = process(path)
        n = n_cities(text)
        pop = extract(text)
        full_pop.extend(pop)
        if len(pop) != n:
            print("ERROR:", path)
            print(n)
            print(len(pop))
            print(pop)
        for city, p in pop:
            if p == 0 or p is None:
                print(city, p)


#%%
import pandas as pd
from krasnodar import yield_full_population
from tqdm import tqdm

gen = tqdm(yield_full_population("rar"))
df = pd.DataFrame(gen, columns=["city", "population", "region_name"])
# WAIT: retrieve fileds from dadata
#       condition - make sure proxy region mateches 'region_iso_code'
#       (will violate if 2 cities have same name)
df["lat"] = None
df["lon"] = None
df["federal_district"] = None
df["region_iso_code"] = None
df["fias_id"] = None
df["kladr_id"] = None

#%%
df.sort_values(["region_name", "city"]).to_csv("towns.csv", index=False)

# %%
# Use for screening a region:
from krasnodar import process

text = process("rar/1.11_Московская область.docx")
# print(text)



# %%
