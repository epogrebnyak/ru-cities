# ru-cities

1117 Russian cities, with population estimates (as of 2020-01-01) and city center geographic coordinates.

## Files and columns

1. towns.csv:

- `city_name`
- `population` - Rosstat estimate, thousand people, as of 1.1.2020
- `region_name` - subnational region (oblast, republic or krai)

To be added (via dadata.ru and OSM):

- `lat,lon` - geographic coordinates (from OSM)
- `federal_district`, eg "Центральный"
- `region_iso_code` - [ISO 3166 code](https://en.wikipedia.org/wiki/ISO_3166-2:RU), eg `RU-VLD`
- `fias_id` - `код ФИАС`
- `kladr_id` - `код КЛАДР` (depreciated)
- `place_id` - OpenStreetMap (OSM) identifier

2. regions.csv - list of Russian Federation regions

## Sources

- City list and city population collected from Rosstat publication [Регионы России. Основные социально-экономические показатели городов](https://rosstat.gov.ru/folder/210/document/13206) and parsed from publication Microsoft Word files.

- City list verified against [Wikipedia article](https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8).

## Comments

- `Белоозерский` not found in Rosstat publication, but [should be considered a city as of 1.1.2020](https://github.com/epogrebnyak/ru-cities/issues/5#issuecomment-886179980)

- `Дмитриев` and `Дмитриев-Льговский` are the same city.

- `Ханты-Мансийский` and `Ямало-Ненецкий` autonomous regions excluded to avoid duplication
  (parts of `Тюменская область`).

- Several notable towns are classified as administrative part of larger cities (eg `Сестрорецк` is a municpality at  `Санкт-Петербург`) and not reported in this dataset.
