"""Геокодирование https://dadata.ru/api/clean/address/"""

#%%
import requests_cache

requests_cache.install_cache("cache1")

from dadata import Dadata

# TODO: use dotenv
token = "e4d13f85995eb558da51fdb8ef378d5b0d4b516a"
secret = "72d7e7df432ffa0324a2c5ea60fc16422f5971cd"
dadata = Dadata(token, secret)

#%%


def clean(s):
    return dadata.clean("address", s)


def geocode(city, region=""):
    query = "город " + city + ", " + region
    res = dadata.clean("address", query)
    fields = [
        "city",
        "geo_lat",
        "geo_lon",
        "region",
        "region_iso_code",
        "federal_district",
        "capital_marker",
        "okato",
        "oktmo",
        "kladr_id",
        "fias_id",
        "unparsed_parts",
    ]
    out = {f: res[f] for f in fields}
    out["query_city"] = city
    out["query_region"] = region
    return out


# %%
if __name__ == "__main__":
    # %%
    clean("город Ноябрьск Тюменская область")

    # %%
    clean("Заозерный Красноярский край")

    # %%
    clean("город Фрязино, Московская область")

    # %%

    # dadata.clean("address", "Советск")
    # dadata.clean("address", "Советск Калининградская область")
    clean("город Дубна, Московская область")

    # %%
    dadata.clean("address", "Дубна, Московская область")
    geocode("город Дубна, Московская область")

    # %%
    x = geocode("Советск", "Калининградская область")
    assert x["query_region"].split()[0] == x["region"]
    x

    # %%
