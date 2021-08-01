"""Cоздать файл towns.csv и regions.csv"""

#%%
import pandas as pd
from krasnodar.main import yield_full_population
from tqdm import tqdm

gen = tqdm(yield_full_population("rar"))
df = pd.DataFrame(gen, columns=["city", "population", "region_name"])
df["lat"] = None
df["lon"] = None

# WAIT: retrieve fileds from dadata
#       condition - make sure proxy region matches 'region_iso_code'
#       (will violate if 2 cities have same name)
# This shoudl come from dadata
# df["federal_district"] = None
# df["region_iso_code"] = None
# df["fias_id"] = None
# df["kladr_id"] = None

#%%
# create regions.csv
import csv

df[["region_name"]].drop_duplicates().sort_values("region_name").to_csv(
    "regions.csv", header=False, index=False, quoting=csv.QUOTE_ALL
)

# %%
