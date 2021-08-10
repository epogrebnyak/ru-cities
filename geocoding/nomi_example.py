# %%

import time

from OSMPythonTools.nominatim import Nominatim

nominatim = Nominatim()


def is_town(x):
    return x["type"] in ["city", "town", "administrative"]


def query(s):
    return nominatim.query(s).toJSON()


def get_city_jsons(city, region):
    xs = query(city + " " + region)
    return [x for x in xs if is_town(x)]


def one_json(js):
    if len(js) > 1:
        print(["JSON is longer than 1 element, city name ambigious", js])
    if len(js) == 0:
        return {"place_id": None, "lat": None, "lon": None}
    j = js[0]
    fields = "place_id lat lon".split()
    return {field: j[field] for field in fields}


def osm(city, region=""):
    # time.sleep(1)
    print(city,region)
    return one_json(get_city_jsons(city, region))


#%%
if __name__ == "__main__":

    # %%
    assert osm("Ноябрьск, Тюменская область") == {
        "place_id": None,
        "lat": None,
        "lon": None,
    }
    # %%
    assert osm("Наро-Фоминск") == {
        "place_id": 258768837,
        "lat": "55.3879473",
        "lon": "36.7398309",
    }

    # %%
    assert osm("Благовещенск", "Амурская область") == {
        "place_id": 259088952,
        "lat": "50.290527",
        "lon": "127.527161",
    }

    # %%
    assert osm("Приморск", "Калининградская область") == {
        "place_id": 309702734,
        "lon": "54.7301946",
        "lat": "20.0044301",
    }

    # %%
    # ys = nominatim.query("Советск, Россия")
    assert [
        y["display_name"] for y in ys.toJSON() if y["type"] in ["city", "town"]
    ] == [y["display_name"] for y in ys.toJSON() if y["type"] in ["city", "town"]]
    [
        "Советск, Советский городской округ, Калининградская область, Северо-Западный федеральный округ, Россия",
        "Советск, городское поселение Советск, Щёкинский район, Тульская область, Центральный федеральный округ, 301205, Россия",
        "Советск, Советский район, Кировская область, Приволжский федеральный округ, 613341, Россия",
    ]
    # %%
    # zs = nominatim.query("Сестрорецк, Россия")
    assert (
        "Санкт-Петербург"
        in nominatim.query("Сестрорецк, Россия").toJSON()[0]["display_name"]
    )

    # %%
