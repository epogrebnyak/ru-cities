"""Анализ датасета towns.csv"""

#%%
import pandas as pd

df = pd.read_csv("towns.csv")

# %%
# показать города с Ё в названии
cf = pd.read_csv("coord_dadata.csv")
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
# TODO: need plot that properly relects geography
#       possibly (transform=...)
df.plot.scatter(x="lon", y="lat", alpha=0.2)
