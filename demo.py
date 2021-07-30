"""Анализ датасета towns.csv"""

#%%
import pandas as pd

df = pd.read_csv("towns.csv")

#%%
# Города с повторяющимися названиями
# 19 городов действительно повторяются в разных областях
# Благовещенск на Дальнем Востоке и в Башкирии, например
# Три раза Советск
df.groupby("city").count().query("population>1")

#%%
ef = df[df.duplicated(["city"], keep=False)].sort_values("city")


def name(df):
    return df["city"] + " " + df["region_name"]


ef.apply(name, axis=1)

#%%
# from geocoding.dadata_example import geocode
from geocoding.nomi_example import osm
from tqdm import tqdm

out = []
gen = df[["city", "region_name"]]
for _, (city, region_name) in tqdm(gen.iterrows()):
    print(city, region_name)
    resp = osm(city, region_name)
    resp["city"] = city
    resp["region_name"] = region_name
    out.append(resp)
pd.DataFrame(out).to_csv("_coord.csv")

#%%
out_ref = [
    {
        "city": "Белогорск",
        "geo_lat": "50.9213415",
        "geo_lon": "128.4739471",
        "region": "Амурская",
        "region_iso_code": "RU-AMU",
        "federal_district": "Дальневосточный",
        "query_region": "Амурская область",
    },
    {
        "city": "Белогорск",
        "geo_lat": "45.057202",
        "geo_lon": "34.5999029",
        "region": "Крым",
        "region_iso_code": "UA-43",
        "federal_district": "Южный",
        "query_region": "Республика Крым",
    },
    {
        "city": "Березовский",
        "geo_lat": "56.9095924",
        "geo_lon": "60.8180907",
        "region": "Свердловская",
        "region_iso_code": "RU-SVE",
        "federal_district": "Уральский",
        "query_region": "Свердловская область",
    },
    {
        "city": "Березовский",
        "geo_lat": "55.6693513",
        "geo_lon": "86.2744459",
        "region": "Кемеровская область - Кузбасс",
        "region_iso_code": "RU-KEM",
        "federal_district": "Сибирский",
        "query_region": "Кемеровская область - Кузбасс",
    },
    {
        "city": "Благовещенск",
        "geo_lat": "50.290659",
        "geo_lon": "127.527198",
        "region": "Амурская",
        "region_iso_code": "RU-AMU",
        "federal_district": "Дальневосточный",
        "query_region": "Амурская область",
    },
    {
        "city": "Благовещенск",
        "geo_lat": "55.0499867",
        "geo_lon": "55.9553186",
        "region": "Башкортостан",
        "region_iso_code": "RU-BA",
        "federal_district": "Приволжский",
        "query_region": "Республика Башкортостан",
    },
    {
        "city": "Гурьевск",
        "geo_lat": "54.770638",
        "geo_lon": "20.6039767",
        "region": "Калининградская",
        "region_iso_code": "RU-KGD",
        "federal_district": "Северо-Западный",
        "query_region": "Калининградская область",
    },
    {
        "city": "Гурьевск",
        "geo_lat": "54.2859263",
        "geo_lon": "85.9475985",
        "region": "Кемеровская область - Кузбасс",
        "region_iso_code": "RU-KEM",
        "federal_district": "Сибирский",
        "query_region": "Кемеровская область - Кузбасс",
    },
    {
        "city": "Железногорск",
        "geo_lat": "52.3380202",
        "geo_lon": "35.3516867",
        "region": "Курская",
        "region_iso_code": "RU-KRS",
        "federal_district": "Центральный",
        "query_region": "Курская область",
    },
    {
        "city": "Железногорск",
        "geo_lat": "56.2529035",
        "geo_lon": "93.532273",
        "region": "Красноярский",
        "region_iso_code": "RU-KYA",
        "federal_district": "Сибирский",
        "query_region": "Красноярский край",
    },
    {
        "city": "Заречный",
        "geo_lat": "56.8102931",
        "geo_lon": "61.3380029",
        "region": "Свердловская",
        "region_iso_code": "RU-SVE",
        "federal_district": "Уральский",
        "query_region": "Свердловская область",
    },
    {
        "city": "Заречный",
        "geo_lat": "53.1960836",
        "geo_lon": "45.1689907",
        "region": "Пензенская",
        "region_iso_code": "RU-PNZ",
        "federal_district": "Приволжский",
        "query_region": "Пензенская область",
    },
    {
        "city": "Киров",
        "geo_lat": "58.6035264",
        "geo_lon": "49.6679304",
        "region": "Кировская",
        "region_iso_code": "RU-KIR",
        "federal_district": "Приволжский",
        "query_region": "Кировская область",
    },
    {
        "city": "Киров",
        "geo_lat": "54.0790111",
        "geo_lon": "34.3076201",
        "region": "Калужская",
        "region_iso_code": "RU-KLU",
        "federal_district": "Центральный",
        "query_region": "Калужская область",
    },
    {
        "city": "Кировск",
        "geo_lat": "67.6150424",
        "geo_lon": "33.663735",
        "region": "Мурманская",
        "region_iso_code": "RU-MUR",
        "federal_district": "Северо-Западный",
        "query_region": "Мурманская область",
    },
    {
        "city": "Кировск",
        "geo_lat": "59.8754216",
        "geo_lon": "30.981364",
        "region": "Ленинградская",
        "region_iso_code": "RU-LEN",
        "federal_district": "Северо-Западный",
        "query_region": "Ленинградская область",
    },
    {
        "city": "Красноармейск",
        "geo_lat": "51.023541",
        "geo_lon": "45.695044",
        "region": "Саратовская",
        "region_iso_code": "RU-SAR",
        "federal_district": "Приволжский",
        "query_region": "Саратовская область",
    },
    {
        "city": "Красноармейск",
        "geo_lat": "56.105426",
        "geo_lon": "38.140838",
        "region": "Московская",
        "region_iso_code": "RU-MOS",
        "federal_district": "Центральный",
        "query_region": "Московская область",
    },
    {
        "city": "Краснознаменск",
        "geo_lat": "55.5978959",
        "geo_lon": "37.0393709",
        "region": "Московская",
        "region_iso_code": "RU-MOS",
        "federal_district": "Центральный",
        "query_region": "Московская область",
    },
    {
        "city": "Краснознаменск",
        "geo_lat": "54.9453423",
        "geo_lon": "22.4928745",
        "region": "Калининградская",
        "region_iso_code": "RU-KGD",
        "federal_district": "Северо-Западный",
        "query_region": "Калининградская область",
    },
    {
        "city": "Краснослободск",
        "geo_lat": "48.7068721",
        "geo_lon": "44.5630857",
        "region": "Волгоградская",
        "region_iso_code": "RU-VGG",
        "federal_district": "Южный",
        "query_region": "Волгоградская область",
    },
    {
        "city": "Краснослободск",
        "geo_lat": "54.4248207",
        "geo_lon": "43.7845011",
        "region": "Мордовия",
        "region_iso_code": "RU-MO",
        "federal_district": "Приволжский",
        "query_region": "Республика Мордовия",
    },
    {
        "city": "Мирный",
        "geo_lat": "62.7645265",
        "geo_lon": "40.3360076",
        "region": "Архангельская",
        "region_iso_code": "RU-ARK",
        "federal_district": "Северо-Западный",
        "query_region": "Архангельская область",
    },
    {
        "city": "Мирный",
        "geo_lat": "62.536232",
        "geo_lon": "113.9667728",
        "region": "Саха /Якутия/",
        "region_iso_code": "RU-SA",
        "federal_district": "Дальневосточный",
        "query_region": "Республика Саха (Якутия)",
    },
    {
        "city": "Михайловск",
        "geo_lat": "45.1297323",
        "geo_lon": "42.0288443",
        "region": "Ставропольский",
        "region_iso_code": "RU-STA",
        "federal_district": "Северо-Кавказский",
        "query_region": "Ставропольский край",
    },
    {
        "city": "Михайловск",
        "geo_lat": "56.4370039",
        "geo_lon": "59.1137316",
        "region": "Свердловская",
        "region_iso_code": "RU-SVE",
        "federal_district": "Уральский",
        "query_region": "Свердловская область",
    },
    {
        "city": "Никольск",
        "geo_lat": "59.5351837",
        "geo_lon": "45.4576137",
        "region": "Вологодская",
        "region_iso_code": "RU-VLG",
        "federal_district": "Северо-Западный",
        "query_region": "Вологодская область",
    },
    {
        "city": "Никольск",
        "geo_lat": "53.7137496",
        "geo_lon": "46.0799857",
        "region": "Пензенская",
        "region_iso_code": "RU-PNZ",
        "federal_district": "Приволжский",
        "query_region": "Пензенская область",
    },
    {
        "city": "Озерск",
        "geo_lat": "55.763154",
        "geo_lon": "60.7076198",
        "region": "Челябинская",
        "region_iso_code": "RU-CHE",
        "federal_district": "Уральский",
        "query_region": "Челябинская область",
    },
    {
        "city": "Озерск",
        "geo_lat": "54.4084705",
        "geo_lon": "22.0134438",
        "region": "Калининградская",
        "region_iso_code": "RU-KGD",
        "federal_district": "Северо-Западный",
        "query_region": "Калининградская область",
    },
    {
        "city": "Приморск",
        "geo_lat": "60.3660209",
        "geo_lon": "28.6135772",
        "region": "Ленинградская",
        "region_iso_code": "RU-LEN",
        "federal_district": "Северо-Западный",
        "query_region": "Ленинградская область",
    },
    {
        "city": "Приморск",
        "geo_lat": "54.7311437",
        "geo_lon": "19.9981926",
        "region": "Калининградская",
        "region_iso_code": "RU-KGD",
        "federal_district": "Северо-Западный",
        "query_region": "Калининградская область",
    },
    {
        "city": "Радужный",
        "geo_lat": "62.1342888",
        "geo_lon": "77.4584094",
        "region": "Ханты-Мансийский Автономный округ - Югра",
        "region_iso_code": "RU-KHM",
        "federal_district": "Уральский",
        "query_region": "Тюменская область",
    },
    {
        "city": "Радужный",
        "geo_lat": "55.9960277",
        "geo_lon": "40.3321855",
        "region": "Владимирская",
        "region_iso_code": "RU-VLA",
        "federal_district": "Центральный",
        "query_region": "Владимирская область",
    },
    {
        "city": "Советск",
        "geo_lat": "55.0809336",
        "geo_lon": "21.8886106",
        "region": "Калининградская",
        "region_iso_code": "RU-KGD",
        "federal_district": "Северо-Западный",
        "query_region": "Калининградская область",
    },
    {
        "city": "Советск",
        "geo_lat": "53.9338874",
        "geo_lon": "37.6316141",
        "region": "Тульская",
        "region_iso_code": "RU-TUL",
        "federal_district": "Центральный",
        "query_region": "Тульская область",
    },
    {
        "city": "Советск",
        "geo_lat": "57.584196",
        "geo_lon": "48.9590272",
        "region": "Кировская",
        "region_iso_code": "RU-KIR",
        "federal_district": "Приволжский",
        "query_region": "Кировская область",
    },
    {
        "city": "Фокино",
        "geo_lat": "42.9706317",
        "geo_lon": "132.4110196",
        "region": "Приморский",
        "region_iso_code": "RU-PRI",
        "federal_district": "Дальневосточный",
        "query_region": "Приморский край",
    },
    {
        "city": "Фокино",
        "geo_lat": "53.4554145",
        "geo_lon": "34.4159238",
        "region": "Брянская",
        "region_iso_code": "RU-BRY",
        "federal_district": "Центральный",
        "query_region": "Брянская область",
    },
]


# TODO: use data to add extra information
# TODO: add 'RU-SAR' from dadata
# TODO: add city coordinates from dadata


# WAIT: move to stand-alone repo
# WAIT: draw on country map
# WAIT: make canonic dataset and add zenodo

# WAIT: match with SDEK city list - see demo at sdek.py

# NOTE: Сестрорецк, Щербинка are inside larger cities

# %%
