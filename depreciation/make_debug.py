# %%
import pandas as pd
from krasnodar.main import (
    docx_files,
    extract,
    n_cities,
    process,
)

# %%
# NOTE: rar folder is populated with rar/get.sh
if False:
    full_pop = []
    for path in docx_files("rar"):
        text = process(path)
        n = n_cities(text)
        pop = extract(text)
        full_pop.extend(pop)
        if len(pop) != n:
            print("ERROR:", path)
            print(n)
            print(len(pop))
            print(pop)
        for city, p in pop:
            if p == 0 or p is None:
                print(city, p)


# %%
# Use for screening a region:
from krasnodar import process

text = process("rar/1.11_Московская область.docx")
# print(text)
