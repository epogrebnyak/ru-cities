"""Cоздать файлы:
   _towns.csv
   assets/regions.csv
"""

#%%
import pandas as pd
from tqdm import tqdm

from krasnodar.main import yield_full_population
from krasnodar.main import yield_ao_population


gen = tqdm(yield_full_population("rar"))
df = pd.DataFrame(gen, columns=["city", "population", "region_name"])
df = df.sort_values(["region_name", "city"])


af = pd.DataFrame(
    yield_ao_population("rar"), columns=["city", "population", "region_name_ao"]
)
ao_to_region_dict = {
    "Ямало-Ненецкий автономный округ": "Тюменская область",
    "Ханты-Мансийский автономный округ – Югра": "Тюменская область",
    "Ненецкий автономный округ": "Архангельская область",
}
af["region_name"] = af.region_name_ao.apply(lambda r: ao_to_region_dict[r])
assert len(af) == (16 + 8 + 1)

df = df.merge(
    af[["city", "region_name", "region_name_ao"]],
    how="left",
    left_on=["city", "region_name"],
    right_on=["city", "region_name"],
)
# We assume population figure is right in AO.

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
