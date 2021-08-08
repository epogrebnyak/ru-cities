"""Cоздать файлы:
   _towns.csv
   assets/regions.csv
"""

#%%
import pandas as pd
from tqdm import tqdm

from krasnodar.main import yield_full_population

gen = tqdm(yield_full_population("rar"))
df = pd.DataFrame(gen, columns=["city", "population", "region_name"])
df = df.sort_values(["region_name", "city"])
filename = "_towns.csv"
df.to_csv(filename, index=False)
print(f"Created {filename}")

#%%
import csv
from helper import local_path

filename = local_path("regions.csv")
rf = df[["region_name"]].drop_duplicates().sort_values("region_name")
rf.to_csv(filename, header=False, index=False, quoting=csv.QUOTE_ALL)
print(f"Created {filename}")
