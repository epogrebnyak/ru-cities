"""Cоздать файл towns.csv и regions.csv"""

#%%
import pandas as pd
from tqdm import tqdm

from krasnodar.main import yield_full_population

gen = tqdm(yield_full_population("rar"))
df = pd.DataFrame(gen, columns=["city", "population", "region_name"])

#%%
df.sort_values(["region_name", "city"]).to_csv("towns.csv", index=False)
print("Created towns.csv")


#%%
# create regions.csv
import csv

df[["region_name"]].drop_duplicates().sort_values("region_name").to_csv(
    "regions.csv", header=False, index=False, quoting=csv.QUOTE_ALL
)
print("Created regions.csv")

# %%
