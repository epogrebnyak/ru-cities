"""Cоздать файл assets/towns.csv"""
# %%
import pandas as pd


df = pd.read_csv("_towns.csv")
cf = pd.read_csv("geocoding/coord_dadata.csv")
# %%


# %%
cols = [
    "city_x",
    "population",
    "geo_lat",
    "geo_lon",
    "region_name",
    "region_name_ao",
    "region_iso_code",
    "federal_district",
    "okato",
    "oktmo",
    "kladr_id",
    "fias_id",
]

# %%
df2 = df.merge(
    cf, left_on=["city", "region_name"], right_on=["query_city", "query_region"]
)[cols].rename(columns=dict(geo_lat="lat", geo_lon="lon", city_x="city"))

# %%
# Fix Нарьян-Мар
ix = df2[df2.city == "Нарьян-Мар"].index[0]
df2.loc[ix, "lat"] = 67.63777777777779
df2.loc[ix, "lon"] = 53.00666666666667
df2.loc[ix]

# %%
from helper import local_path

filename = local_path("towns.csv")
df2.sort_values(["region_name", "city"]).to_csv(filename, index=False)
print(f"Wrote {filename}")
# %%
