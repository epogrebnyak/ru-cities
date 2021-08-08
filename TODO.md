## Next

Done:

- [x] Compare OSM and dadata outputs (distances form city centers)

Using the dataset:

- [-] Draw a map of Russian towns (see demo.py) (#6)

'place_id' https://github.com/epogrebnyak/ru-cities/issues/10:

- [-] Merge OSM `place_id` to dataset - # поменять place_id Сычевки Смоленская обалсть 3377406

Add more columns to towns.csv:

`is_capital` - https://github.com/epogrebnyak/ru-cities/issues/9

- [ ] make region list from text file, wikipedia or api-crafter
- [ ] make a test about region count
- [ ] add `is_capital` (1 or 0) column for region capitals
- [ ] decide if `is_capital` should be 1 for AO

`region_name_ao` - https://github.com/epogrebnyak/ru-cities/issues/8

- [-] add `region_name_ao` to dataset

  - [-] follow how towns.csv is created (especially add_after())
  - [-] Restore `Ханты-Мансийский` and `Ямало-Ненецкий` АО,
  - [-] The above will fix Нарьян-Мар in coord_dadata.csv

New datasets:

- [ ] region info (GDP, population, retail turnover)
- [ ] parse retail turnover by city from Rosstat
- [ ] SDEK tags for city names
- [ ] Large municipalities (Сестрорецк, Щербинка)

Russian cities - excercise list:

- cluster cities to new regions
- cluster cites around largest cities or region capitals
- calculate distances between regions
- (...)
