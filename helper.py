# %%
from pathlib import Path
import json


def local_path(filename):
    return Path("assets") / filename


def to_json(x, path):
    Path(path).write_text(json.dumps(x, ensure_ascii=False, indent=4), encoding="utf-8")

def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))
