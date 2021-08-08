import re
from pathlib import Path

import requests
from docx2txt import process


def filename(url):
    return url.split("/")[-1]


def save(url):
    path = filename(url)
    if not Path(path).exists():
        r = requests.get(url)
        Path(path).write_bytes(r.content)
    return path


def split(line):
    try:
        city, pop = line.split("–")
    except ValueError:
        return line, None
    city = city.strip()
    try:
        pop = float(pop.strip().replace(")", "").replace(",", "."))
    except ValueError:
        pop = None
    return city, pop


def yield_values(text):
    fa, fb = False, False
    has_worked = False
    for line in text.split("\n"):
        if "Города" in line:
            fa = True
        if fa and ("численность населения" in line or "численность жителей" in line):
            fb = True
            continue
        # start parsing after encountered
        # both "Города" and "численность населения"
        if fa and fb and "–" in line:
            has_worked = True
            yield (split(line))
        # end parsing if encounted
        # next header, sometimes the header is missplaced
        if has_worked and "Площадь территории" in line:
            break
        if has_worked and "Плотность населения" in line:
            break
        if (
            has_worked
            and "ГРУППИРОВКА ГОРОДОВ ПО ЧИСЛЕННОСТИ ПОСТОЯННОГО НАСЕЛЕНИЯ" in line
        ):
            break


def extract(text):
    return list(yield_values(text))


def get_population(path):
    return extract(process(path))


def n_cities(text):
    return int(re.search(r"Города –\s*(\d*)", text).groups()[0])


def get_region_name(text):
    region_name = str.strip(re.search(r"\n(.*?)\n\nвсе население", text).groups()[0])
    region_name = re.sub(" +", " ", region_name)
    if "Люберцы" in region_name:
        region_name = "Московская область"
    return region_name


def must_exclude(path):
    excludes = [
        "Ненецкий",  # часть Астраханской области
        "Ханты-Мансийский",  # часть Тюменской области
        "Ямало-Ненецкий",  # часть Тюменской области
        "Саратовская",
        "Камчатский край",
        " фо",
        "Севастополь",
        "Москва",
        "Петербург",
        "7.2_Республика  Алтай",
    ]
    f1 = str(path).startswith("~")
    f2 = any([x in str(path) for x in excludes])
    return f1 or f2


def all_docx_files(folder):
    return Path(folder).glob("*.docx")


def docx_files(folder):
    for path in all_docx_files(folder):
        if not must_exclude(path):
            yield path


def docx_files_ao_subordinate(folder):
    for path in all_docx_files(folder):
        path_str = str(path)
        if (
            ("Ненецкий" in path_str)
            or ("Ханты-Мансийский" in path_str)
            or ("Ямало-Ненецкий" in path_str)
        ):
            yield path


supplement_dict = {
    "Москва": [("Москва", 12655.1)],
    "Санкт-Петербург": [("Санкт-Петербург", 5384.3)],
    "Севастополь": [("Севастополь", 510.0)],
    "Московская область": [("Белоозерский", 17.898)],
    "Камчатский край": [
        ("Петропавловск-Камчатский", 179.6),
        ("Елизово", 39.3),
        ("Вилючинск", 22.2),
    ],
    "Саратовская область": [
        ("Саратов", 838.0),
        ("Аткарск", 24.1),
        ("Энгельс", 227.0),
        ("Красноармейск", 22.3),
        ("Балаково", 187.5),
        ("Ершов", 18.8),
        ("Балашов", 75.8),
        ("Новоузенск", 15.1),
        ("Вольск", 61.9),
        ("Калининск", 15.6),
        ("Пугачев", 40.6),
        ("Красный Кут", 14.1),
        ("Ртищево", 38.4),
        ("Хвалынск", 12.3),
        ("Маркс", 30, 7),
        ("Аркадак", 11.5),
        ("Петровск", 28.2),
        ("Шиханы", 5.4),
    ],
    "Республика Алтай": [("Горно-Алтайск", 64.5)],
}


def add_after():
    for k, vs in supplement_dict.items():
        for v in vs:
            yield v[0], v[1], k


def change(city: str):
    return "Сергиев Посад" if city == "Сергиев-Посад" else city


def yield_from(folder, gen_func):
    for path in gen_func(folder):
        text = process(path)
        region_name = get_region_name(text)
        for city, pop in extract(text):
            yield change(city), pop, region_name


def yield_full_population(folder):
    for (city, pop, region_name) in yield_from(folder, docx_files):
        yield city, pop, region_name
    for (city, pop, region_name) in add_after():
        yield city, pop, region_name


def yield_ao_population(folder):
    for (city, pop, region_name) in yield_from(folder, docx_files_ao_subordinate):
        if city == "Ненецкий автономный округ":  # stub / костыль
            continue
        if city == "Нарьян-Мар":
            yield "Нарьян-Мар", 25.1, "Ненецкий автономный округ"
            continue
        yield city, pop, region_name
