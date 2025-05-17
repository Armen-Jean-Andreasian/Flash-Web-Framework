from functools import lru_cache
from pathlib import Path
import json
import os


@lru_cache(maxsize=128)
def cache_n_render_json(fp):
    try:
        with open(fp, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        return {"error": "Invalid JSON", "details": str(e)}
    except Exception as e:
        return {"error": "File read failed", "details": str(e)}


def render_json(jfp):
    path = Path(jfp)

    if not path.exists():
        return {"error": "File not found", "path": str(jfp)}

    if os.path.getsize(jfp) > 1_000_000:
        try:
            with open(jfp, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            return {"error": "Large file read failed", "details": str(e)}

    return cache_n_render_json(jfp)
