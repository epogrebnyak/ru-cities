"""Проверить дают ли dadata и OSM близкие координаты городов."""

import pandas as pd
from math import radians, cos, sin, asin, sqrt
from pathlib import Path


def haversine(lon1, lat1, lon2, lat2):

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    return km


# гарантировать запуск из других каталогов
this_dir = Path(__file__).parent
root = this_dir.parent

df1 = pd.read_csv(
    root / "assets" / "towns.csv", usecols=["city", "region_name", "lat", "lon"]
)

df2 = pd.read_csv(
    root / "geocoding" / "coord_osm.csv",
    usecols=["query_city", "query_region", "lat", "lon"],
).rename(columns={"query_city": "city", "query_region": "region_name"})

df3 = df1.merge(
    df2[["city", "region_name", "lat", "lon"]],
    how="outer",
    left_on=["city", "region_name"],
    right_on=["city", "region_name"],
)

df3["distance_km"] = df3.apply(
    lambda row: haversine(row["lon_x"], row["lat_x"], row["lon_y"], row["lat_y"]),
    axis=1,
)

df3 = df3.sort_values(by=["distance_km"], ascending=False).query("distance_km > 5")

df3.to_csv(this_dir / "similarity_check.csv")


# Наибольшее расхождение:

"""
,city,region_name,lat_x,lon_x,lat_y,lon_y,distance_km
933,Сычевка,Смоленская область,55.8308821,34.2778793,54.356365,32.08746,215.17183787002423
"""

# Сычевка,Смоленская область
# wiki: 55°50′ с. ш. 34°17′ в. д.
# yandex: 55.828542, 34.277748
# - place_id (OSM) Сычевки 3377406
# дадата выдает правильные координаты
# OSM дал координаты деревни Сычевка в той же области
# OSM знает город, но считает что это "Сычёвка"

# По другим городам считаем, что до 10 км разница в координатах центров незначимая.

# - Координаты в датасете towns.csv правильные.
# - можно улушить датасет OSM, если:
#   - добавить букву ё через
#   - использовать "автономная обалсть" и "автономный округ" в названиях региона
