#%%

import os
from pathlib import Path

import pandas as pd
from krasnodar import (
    add_after,
    docx_files,
    extract,
    get_population,
    get_region_name,
    n_cities,
    process,
    save,
    split,
)
from reference import cities_2010, region_list

url = "https://gks.ru/bgd/regl/b20_14t/IssWWW.exe/Stg/ug/krasnod.docx"
path = save(url)

base = Path(os.path.dirname(__file__))
text_msk = (base / "msk.txt").read_text(encoding="utf-8")

df = pd.read_csv(base / "towns.csv")


#%%
# TODO: переделать в тест
def test_df_fornull():
    assert len(df[df.population.isna()]) == 0
    assert len(df[df.population == 0]) == 0


#%%
def test_vs_citilist_2010():
    assert {"Дмитриев"} == set(cities_2010) - set(df.city.tolist())
    assert {"Дмитриев-Льговский"} == set(df.city.tolist()) - set(cities_2010)


#%%
def test_region_names():
    assert df.region_name.isin(region_list).all()


#%%
def test_columns():
    assert df.columns.tolist() == [
        "city",
        "population",
        "region_name",
        "lat",
        "lon",
        "federal_district",
        "region_iso_code",
        "fias_id",
        "kladr_id",
    ]


#%%


def test_gorno_altaisk():
    assert "Горно-Алтайск" in df.city.tolist()


def test_sergiev_posad():
    assert "Сергиев Посад" in df.city.tolist()
    assert "Сергиев-Посад" not in df.city.tolist()


#%%
def test_total_cities_count():
    assert len(df) == 1117


def test_add_after():
    assert len(list(add_after())) >= 24


def test_get_region_name_works_on_msk_obl():
    assert get_region_name(text_msk) == "Московская область"


def test_save():
    assert path == "krasnod.docx"


def test_split1():
    assert split("Горячий Ключ – 40,3") == ("Горячий Ключ", 40.3)


def test_split2():
    assert split("Куртамыш –16,5") == ("Куртамыш", 16.5)


def test_get_population():
    assert get_population(path) == [
        ("Краснодар", 932.6),
        ("Белореченск", 51.6),
        ("Сочи", 443.6),
        ("Тимашевск", 50.8),
        ("Новороссийск", 275.0),
        ("Курганинск", 48.2),
        ("Армавир", 189.0),
        ("Кореновск", 42.4),
        ("Анапа", 88.9),
        ("Темрюк", 41.4),
        ("Ейск", 83.1),
        ("Горячий Ключ", 40.3),
        ("Кропоткин", 77.7),
        ("Апшеронск", 39.5),
        ("Геленджик", 76.8),
        ("Усть-Лабинск", 39.5),
        ("Славянск-на-Кубани", 67.9),
        ("Абинск", 39.1),
        ("Туапсе", 61.2),
        ("Новокубанск", 35.2),
        ("Лабинск", 59.3),
        ("Гулькевичи", 34.3),
        ("Крымск", 57.9),
        ("Приморско-Ахтарск", 32.3),
        ("Тихорецк", 57.1),
        ("Хадыженск", 22.2),
    ]


def test_city_count():
    for path in docx_files("rar"):
        text = process(path)
        n = n_cities(text)
        pop = extract(text)
        assert len(pop) == n