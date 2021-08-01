"""Анализ датасета towns.csv"""

#%%
import pandas as pd

df = pd.read_csv("towns.csv")


# %%
df = pd.read_csv("towns.csv")
df.groupby("city").count().query("population>1")

#%%
# Города с повторяющимися названиями
# 19 городов действительно повторяются в разных областях
# Благовещенск на Дальнем Востоке и в Башкирии, например
# Три раза Советск
df[df.duplicated(["city"], keep=False)].sort_values("city")


# %%
