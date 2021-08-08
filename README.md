# ru-cities

![GitHub release (latest by date)](https://img.shields.io/github/v/release/epogrebnyak/ru-cities)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5151423.svg)](https://doi.org/10.5281/zenodo.5151423)
[![](https://img.shields.io/badge/API_Crafter-ru--cities--db-blue)](https://beta.apicrafter.ru/packages/ru-cities-db)

1117 Russian cities with geographic coordinates, identifiers and 2020 population estimate.

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
- [alt_city_names.json](assets/alt_city_names.json) - alternative city names

## Сolumns (towns.csv):

Basic info:

- `city` - city name (several cities have alternative names marked in `alt_city_names.json`)
- `population` - city population, thousand people, Rosstat estimate as of 1.1.2020
- `lat,lon` - city geographic coordinates

Region:

- `region_name` - subnational region name: oblast, republic, krai or one AO (Chukotka)
- `region_name_ao` - autonomous okrug (AO) name, if AO is a part of larger regions (applies to 3 AO)
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

#### Autonomous regions (AO)

There are four autonomous regions (AO) in Russia:

- Ненецкий автономный округ
- Ханты-Мансийский автономный округ - Югра
- Чукотский автономный округ
- Ямало-Ненецкий автономный округ

`Ханты-Мансийский` and `Ямало-Ненецкий` (AO) are inner parts of `Тюменская область`.
`Ненецкий` autonomous regions (AO) is inner part of `Архангельская область`.
AO names above are listed in `region_name_ao` for three AO.

`Чукотский` AO is a stand-alone region, it is not an inner part of any region.
`Чукотский автономный округ` is listed in `region_name` only.

#### Smaller cities

- Several notable towns are classified as administrative part of larger cities (`Сестрорецк` is a municpality at Saint-Petersburg, `Щербинка` is a part of larger Moscow). They are not reported in this dataset.

#### Individual cities

- `Белоозерский` not found in Rosstat publication, but [should be considered a city as of January 1, 2020](https://github.com/epogrebnyak/ru-cities/issues/5#issuecomment-886179980). We included it into dataset.

#### Alternative city names

- `Дмитриев` and `Дмитриев-Льговский` are the same city.
- We suppressed letter "ё" `city` columns in towns.csv - we have `Орел`, but not `Орёл`. This affected, for example:
  - `Белоозёрский`
  - `Королёв`
  - `Ликино-Дулёво`
  - `Озёры`
  - `Щёлково`
  - `Орёл`

`assets/alt_city_names.json` contains the alternative name pairing.

## Tests

```
poetry install
poetry run python -m pytest
```

## How to replicate dataset

#### 1. Base dataset

Run:

- download data from Rosstat using rar/get.sh
- convert `Саратовская область.doc` to docx
- run make.py

Creates:

- `_towns.csv`
- `assets/regions.csv`

#### 2. API calls

Note: do not attempt this stage if you do not have to - these scripts take a while
and use third-party API access. You have the resulting files in repo, so probably
you can skip running these scripts.

Run:

- `cd geocoding`
- run coord_dadata.py (needs token)
- run coord_osm.py

Creates:

- geocoding/coord_dadata.csv
- geocoding/coord_osm.csv

#### 3. Merge data

Run:

- run merge.py

Creates:

- assets/towns.csv
