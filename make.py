"""Cоздать файлы
 _towns.csv
 assets/regions.csv
 assets/alt_region_names.json"""

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

# %%
from helper import local_path, to_json

# В основе - "coord_dadata.csv" 
# cf.city != cf.query_city
alt_city_names = {
    "Дмитриев-Льговский": "Дмитриев",
    "Белоозерский": "Белоозёрский",
    "Королев": "Королёв",
    "Ликино-Дулево": "Ликино-Дулёво",
    "Озеры": "Озёры",
    "Щелково": "Щёлково",
    "Орел": "Орёл",
}
path = local_path("alt_city_names.json")
to_json(alt_city_names, path)
print(f"Created {path}")

# %%
