from pathlib import Path
import requests
import pandas as pd

url = ("https://raw.githubusercontent.com/"
      "epogrebnyak/ru-cities/main/towns.csv")

# save file locally
p = Path("towns.csv")
if not p.exists():
    content = requests.get(url).text
    p.write_text(content, encoding="utf-8")

# read as dataframe
df = pd.read_csv("towns.csv")
print(df.sample(5))
