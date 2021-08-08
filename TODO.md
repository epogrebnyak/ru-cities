## Next

Done:

- [x] Compare OSM and dadata outputs (distances form city centers)

Using the dataset:

- [-] Draw a map of Russian towns (see demo.py) (#6)

- [-] Merge OSM `place_id` to dataset - # поменять place_id Сычевки Смоленская обалсть 3377406
     

Add more columns to towns.csv:
- [ ] Add `is_capital` (1 or 0) column for region capitals
- [-] add `region_name_ao` to dataset
   - [-] follow how towns.csv is created (especially add_after()) 
   - [-] Restore `Ханты-Мансийский` and `Ямало-Ненецкий` АО, add which regions
    are contained in other regions.
  -  [-] The above will fix Нарьян-Мар in coord_dadata.csv
 
New datasets:

- [ ] parse retail turnover by city from Rosstat
- [ ] SDEK tags for city names
- [ ] Large municipalities (Сестрорецк, Щербинка)
