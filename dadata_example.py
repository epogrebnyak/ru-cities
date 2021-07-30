#%%
import requests_cache
#requests_cache.install_cache()

from dadata import Dadata

token = "3b44926e01ec647f877ad1e9dac59b8ba2115f08"
secret = "aec35c7b9c90f01a6585b8c79ee32a3c130f9163"
dadata = Dadata(token, secret)
# %%

# dadata.clean("address", "Советск")
dadata.clean("address", "Советск Калининградская область")
# %%

def geocode(city, region=""):
    query = city+" "+region
    res = dadata.clean("address", query)
    assert res["unparsed_parts"] is None   
    assert res["city"] == city
    fields = ['city', 'geo_lat', 'geo_lon', 'region', 'region_iso_code', 'federal_district']
    out =  {f:res[f] for f in fields}
    out["query_region"] = region
    return out


x = geocode("Советск", "Калининградская область")
assert x["query_region"].split()[0] == x["region"]
x


# %%
