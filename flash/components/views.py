from flash.components.exceptions import PathOccupied
from flash.types import HttpMethod, ContentType
from typing import Callable
from dataclasses import dataclass


@dataclass
class ViewData:
    path: str
    content_type: ContentType
    http_method: HttpMethod
    callback: Callable

    def __post_init__(self):
        if not self.path or not isinstance(self.path, str):
            raise ValueError("Path must be a non-empty string")
        if not isinstance(self.content_type, ContentType):
            raise ValueError("Invalid content type")
        if not isinstance(self.http_method, HttpMethod):
            raise ValueError("Invalid HTTP method")
        if not callable(self.callback):
            raise ValueError("Callback must be callable")


class Views:
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
