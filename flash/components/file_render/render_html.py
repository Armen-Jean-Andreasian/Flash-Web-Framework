from functools import lru_cache
from pathlib import Path
import os


@lru_cache(maxsize=128)
def cache_n_render_html(hfp):
    try:
        with open(hfp, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"HTML file can not be rendered. Exception: {e}"


def render_html(fp):
    if not Path(fp):
        return f"HTML file wasn't found. File path: {fp}"

    if os.path.getsize(fp) > 1_000_000:  # no caching if >1 MB
        return open(fp).read()

    return cache_n_render_html(fp)
