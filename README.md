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
      "epogrebnyak/ru-cities/main/assets/towns.csv")

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

- [towns.csv](assets/towns.csv) - city information
- [regions.csv](assets/regions.csv) - list of Russian Federation regions
- [alt_city_names.json](assets/alt_city_names.json) - several alternative city names

## Сolumns (towns.csv):

Basic info:

- `city` - city name (several cities have alternative names marked in `alt_city_names.json`)
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
- `kladr_id`

## Data sources

- City list and city population collected from Rosstat publication [Регионы России. Основные социально-экономические показатели городов](https://rosstat.gov.ru/folder/210/document/13206) and parsed from publication Microsoft Word files.
- City list corresponds to [this Wikipedia article](https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8).
- Alternative dataset is [wiki-based Dadata city dataset](https://github.com/hflabs/city) (no population data).

## Comments

#### City groups

- `Ханты-Мансийский` and `Ямало-Ненецкий` autonomous regions excluded to avoid duplication as parts of `Тюменская область`.

- Several notable towns are classified as administrative part of larger cities (`Сестрорецк` is a municpality at  Saint-Petersburg, `Щербинка` part of Moscow). They are not and not reported in this dataset.

#### By individual city

- `Белоозерский` not found in Rosstat publication, but [should be considered a city as of 1.1.2020](https://github.com/epogrebnyak/ru-cities/issues/5#issuecomment-886179980)

#### Alternative city names

- We suppressed letter "ё" `city` columns in towns.csv - we have `Орел`, but not `Орёл`. This affected:
  - `Белоозёрский`
  - `Королёв`
  - `Ликино-Дулёво`
  - `Озёры`
  - `Щёлково`
  - `Орёл`

- `Дмитриев` and `Дмитриев-Льговский` are the same city.

`assets/alt_city_names.json` contains these names.

## Tests

```
poetry install
poetry run python -m pytest
```

## How to replicate dataset

#### 1. Base dataset

Run:

- download data stro rar/get.sh
- convert `Саратовская область.doc` to docx
- run make.py

Creates:

- `_towns.csv`
- `assets/regions.csv`

#### 2. API calls

Note: do not attempt if you do not have to - this runs a while and loads third-party API access. 

You have the resulting files in repo,
so probably does not need to  these scripts.

Run:

- `cd geocoding`
- run coord_dadata.py (needs token)
- run coord_osm.py

Creates:

- coord_dadata.csv
- coord_osm.csv

#### 3. Merge data

Run:

- run merge.py

Creates:

- assets/towns.csv
