from exceptions import PathOccupied
from _types import HttpMethod, ContentType
from typing import Callable
from pydantic import BaseModel, constr


class ViewData(BaseModel):
    path: constr(min_length=1)
    content_type: ContentType
    http_method: HttpMethod
    callback: Callable


class ViewKeeper:
    def __init__(self):
        self.registered_views: dict[str, ViewData] = dict()  # path : data

    def add_view(
        self,
        path: str,
        content_type: ContentType,
        http_method: HttpMethod,
        callback: Callable
    ):
        if path not in self.registered_views:
            self.registered_views[path] = ViewData(
                path=path,
                content_type=content_type,
                http_method=http_method,
                callback=callback
            )
        else:
            raise PathOccupied(path)

    def __contains__(self, item):
        return item in self.registered_views

    def get(self, path) -> ViewData | None:
        return self.registered_views.get(path)

    @property
    def registered_paths(self) -> dict[str, str]:
        return {k: v.http_method.value for k, v in self.registered_views.items()}
