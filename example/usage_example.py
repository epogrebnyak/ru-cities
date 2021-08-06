from pathlib import Path

import pandas as pd
import requests

url = "https://raw.githubusercontent.com/epogrebnyak/ru-cities/main/assets/towns.csv"

# save file locally
p = Path("towns.csv")
if not p.exists():
    content = requests.get(url).text
    p.write_text(content, encoding="utf-8")

# read as dataframe
df = pd.read_csv("towns.csv")
print(df.sample(5))
