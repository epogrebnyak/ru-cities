#%%
from pathlib import Path
import pandas as pd

# гарантировать запуск из других каталогов
this_dir = Path(__file__).parent
root = this_dir.parent

#%%
df = pd.read_csv(root / "geocoding" / "coord_osm.csv")
df[df.place_id.isna()]


# TODO (Михаил, MT):
# - изменить парсинг папки rar, ввести колонку region_name_ao (непустая для автономных округов)
# - использовать region_name_ao в запросе к OSM
# - использовать alt_city_names.json для городов с ё, расширить alt_city_names.json
# - изменть тип place_id - int или str
# - изменить coord_osm.py, перестроить coord_osm.csv
# - посмотерть что осталось в df[df.place_id.isna()]
# - добавить place_id в towns.csv

# %%
