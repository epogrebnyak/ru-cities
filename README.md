# ru-cities

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5151423.svg)](https://doi.org/10.5281/zenodo.5151423)

1117 Russian cities with city name, region, 
geographic coordinates and 2020 population estimate.

## How to use

```python 
from pathlib import Path
import requests
import pandas as pd

url = ("https://raw.githubusercontent.com/"
      "epogrebnyak/ru-cities/main/towns.csv")

# save file locally
p = Path("towns.csv")
if not p.exists():
    content = requests.get(url).text
    p.write_text(content, encoding="utf-8")

# read as dataframe
df = pd.read_csv("towns.csv")
print(df.sample(5))
```

## Files:

- `towns.csv` - city information
- `regions.csv` - list of Russian Federation regions

## Сolumns (towns.csv):

Basic info:

- `city`
- `population` - city population, thousand people, Rosstat estimate as of 1.1.2020
- `lat,lon` - city geographic coordinates 

Region:

- `region_name` - subnational region (oblast, republic, krai or AO)
- `region_iso_code` - [ISO 3166 code](https://en.wikipedia.org/wiki/ISO_3166-2:RU), eg `RU-VLD`
- `federal_district`, eg `Центральный`

City codes:

- `okato` 
- `oktmo` 
- `fias_id` 
- `kladr_id`  (depreciated)

To be added:

- `place_id` - OpenStreetMap (OSM) identifier
- `is_region_capital` - boolean flag (0 or 1)
- `city_alt_name`


## Sources

- City list and city population collected from Rosstat publication [Регионы России. Основные социально-экономические показатели городов](https://rosstat.gov.ru/folder/210/document/13206) and parsed from publication Microsoft Word files.
- City list corresponds to [this Wikipedia article](https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8).

## Comments

#### City groups

- We suppressed letter "ё" city names - we have `Орел`, but not `Орёл`. This affected:
  - `Белоозёрский`
  - `Королёв`
  - `Ликино-Дулёво`
  - `Озёры`
  - `Щёлково`
  - `Орёл`

- `Ханты-Мансийский` and `Ямало-Ненецкий` autonomous regions excluded to avoid duplication as parts of `Тюменская область`.

- Several notable towns are classified as administrative part of larger cities (`Сестрорецк` is a municpality at  Saint-Petersburg, `Щербинка` part of Moscow). They are not and not reported in this dataset.

#### By individual city

- `Белоозерский` not found in Rosstat publication, but [should be considered a city as of 1.1.2020](https://github.com/epogrebnyak/ru-cities/issues/5#issuecomment-886179980)

- `Дмитриев` and `Дмитриев-Льговский` are the same city.

## Next

- Maybe we should have `city_alt_name` for cases where there are two variants of a city name 
- Restore `Ханты-Мансийский` and `Ямало-Ненецкий` АО
- Compare OSM and dadata outputs (distances form centers)
- Merge OSM `place_id` to dataset 
- Rename `towns.csv` to `cities.csv`
- Draw a map of Russian towns
- SDEK tags for city names
- Large municipalities (Сестрорецк, Щербинка)


## Tests

```
poetry install
poetry run python -m pytest
```

## How to replicate dataset

#### Base dataset

Run:

- download rar/get.sh
- convert `Саратовская область.doc` to docx
- run make.py

Creates:

- towns.csv
- regions.csv

#### Full dataset

Note: do not attempt if you do not have to -
this runs a while and loads third-party API access. 

Run:

- run coord_dadata.py (needs token)
- run coord_osm.py
- run merge.py

Creates:

- coord_dadata.csv
- coord_osm.csv
- towns.csv (overwrites towns.csv with more columns)
