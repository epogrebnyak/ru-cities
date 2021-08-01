# %%
import pandas as pd

df = pd.read_csv("towns.csv")["city population region_name".split()]
cf = pd.read_csv("coord_dadata.csv")
# %%

cf[cf.city.str.contains("ё").fillna(False)].city


# %%
# TODO: mark region capitals
# TODO: mark MOW, SPB, SEV as capitals too

ix = ~cf.capital_marker.isin([1, 0])
ix2 = ~cf.isna()
caps = cf[ix]["city query_region capital_marker".split()]
# assert len(caps) == 82 # breaks, we have 82 regions in regions.csv and 78 in cf


# %%
cols = [
    "city_x",
    "population",
    "geo_lat",
    "geo_lon",
    "region_name",
    "region_iso_code",
    "federal_district",
    "okato",
    "oktmo",
    "kladr_id",
    "fias_id",
    #'capital_marker',
]

# %%
df2 = df.merge(
    cf, left_on=["city", "region_name"], right_on=["query_city", "query_region"]
)[cols].rename(columns=dict(geo_lat="lat", geo_lon="lon", city_x="city"))
print(df2.columns)

# %%
# Fix Нарьян-Мар 
ix = df2[df2.city == "Нарьян-Мар"].index[0]
df2.loc[ix, "lat"] = 67.63777777777779
df2.loc[ix, "lon"] = 53.00666666666667
df2.loc[ix]

# %%
df2.sort_values(["region_name", "city"]).to_csv("towns.csv", index=False)
print("Overwritten towns.csv")

# %%
