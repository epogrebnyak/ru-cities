#%%
from pathlib import Path
import pandas as pd

# гарантировать запуск из других каталогов
this_dir = Path(__file__).parent
root = this_dir.parent

#%%
df = pd.read_csv(root / "geocoding" / "coord_osm.csv").rename(columns={"query_city": "city", "query_region": "region_name"})

df2 = pd.read_csv(root / "assets" / "towns.csv")

print(df[df.place_id.isna()])

# TODO (Михаил, MT):
# https://github.com/epogrebnyak/ru-cities/issues/10
# - [x] изменить парсинг папки rar, ввести колонку region_name_ao (непустая для автономных округов)
# - [x] использовать region_name_ao в запросе к OSM (Open Street Map)
# - [x] использовать alt_city_names.json для городов с ё, расширить alt_city_names.json
# - [x] изменть тип place_id - int или str
# - [x] изменить coord_osm.py, перестроить coord_osm.csv
# - [x] посмотерть что осталось в df[df.place_id.isna()]
# - [x] добавить place_id в towns.csv

df2['place_id'] = df['place_id']
df2.to_csv(root / "assets" / "towns.csv", index=False)


from nomi_example import osm

nothing = {"place_id": None, "lat": None, "lon": None}
assert nothing == osm("Нарьян-Мар", "Архангельская область")

assert {"place_id": 258372341, "lat": "67.6380175", "lon": "53.0071044"} == osm(
    "Нарьян-Мар", "Ненецкий автономный округ"
)
# %%
