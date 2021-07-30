#%%
from OSMPythonTools.nominatim import Nominatim
nominatim = Nominatim()
# %%
ys =  nominatim.query('Советск, Россия')
# %%
assert [y['display_name'] for y in ys.toJSON() if y["type"] in ["city", "town"]] == [y['display_name'] for y in ys.toJSON() if y["type"] in ["city", "town"]]
['Советск, Советский городской округ, Калининградская область, Северо-Западный федеральный округ, Россия',
 'Советск, городское поселение Советск, Щёкинский район, Тульская область, Центральный федеральный округ, 301205, Россия',
 'Советск, Советский район, Кировская область, Приволжский федеральный округ, 613341, Россия']
# %%
zs  = nominatim.query('Сестрорецк, Россия')

# %%
