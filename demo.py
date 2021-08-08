"""Анализ датасета towns.csv"""

# %%
from krasnodar import yield_ao_population
import pandas as pd


af = pd.DataFrame(
    yield_ao_population("rar"), columns=["city", "population", "region_ao_name"]
)
ao_to_region_dict = {
    "Ямало-Ненецкий автономный округ": "Тюменская область",
    "Ханты-Мансийский автономный округ – Югра": "Тюменская область",
    "Ненецкий автономный округ": "Архангельская область",
}
af["region_name"] = af.region_ao_name.apply(lambda r: ao_to_region_dict[r])
assert len(af) == (16 + 8 + 1)
af

#%%
import pandas as pd

df = pd.read_csv("assets/towns.csv")


df.merge(
    af[["city", "region_name", "region_ao_name"]],
    how="left",
    left_on=["city", "region_name"],
    right_on=["city", "region_name"],
)

# assert 0 == len(merged[merged.population_x != merged.population_y])

# %%
# показать города с Ё в названии
cf = pd.read_csv("geocoding/coord_dadata.csv")
x = cf[cf.city.str.contains("ё").fillna(False)][["city", "query_city"]].rename(
    columns=dict(city="alt_city_name")
)

#%%
# Города с повторяющимися названиями
# 19 городов действительно повторяются в разных областях
# Благовещенск на Дальнем Востоке и в Башкирии, например
# Три раза Советск
df[df.duplicated(["city"], keep=False)].sort_values("city")

# %%
df.groupby("city").count().query("population>1")


# %%

# %%
# TODO: mark region capitals
# TODO: mark MOW, SPB, SEV as capitals too
cf = pd.read_csv("geocoding/coord_dadata.csv")
ix = ~cf.capital_marker.isin([1, 0])
ix2 = ~cf.isna()
caps = cf[ix]["city query_region capital_marker".split()]
# assert len(caps) == 82 # breaks, we have 82 regions in regions.csv and 78 in cf

# %%
# TODO: need plot that properly relects geography
#       possibly (transform=...)
df.plot.scatter(x="lon", y="lat", alpha=0.2)
