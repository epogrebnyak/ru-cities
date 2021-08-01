#%%
import pandas as pd
from tqdm import tqdm

from geocoding.dadata_example import geocode

#%%
df = pd.read_csv("towns.csv")
gen = df[["city", "region_name"]]
res = []
for _, (city, region_name) in tqdm(gen.iterrows()):
    x = geocode(city, region_name)
    res.append(x)

mf = pd.DataFrame(res)
mf.to_csv("coord_dadata.csv")


# %%
mf[mf.unparsed_parts.isna()]

# %%
