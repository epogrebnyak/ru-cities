import pandas as pd

# %%
# показать города с Ё в названии
df = pd.read_csv("..\\towns.csv")
cf = pd.read_csv("..\\coord_dadata.csv")
x = (
    cf[cf.city.str.contains("ё").fillna(False)][["city", "query_city"]]
    .rename(columns=dict(city="alt_city_name"))
    .dropna()
)

# %%
y = cf[cf.city != cf.query_city][["city", "query_city"]].dropna()
[(xs[2], xs[1]) for xs in y.to_records()]


# %%
