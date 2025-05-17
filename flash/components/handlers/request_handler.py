import http.server
from typing import Any
import json
from flash.components.views import Views
from flash.types import ContentType
from threading import Lock

__all__ = "RequestHandlerFactory",


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    __views: Views = None
    __lock = Lock()

    def do_GET(self):
        if registered_view := self.__views.get(self.path):
            if registered_view.http_method.value == "GET":
                try:
                    response: Any = registered_view.callback()
                except Exception as err:
                    self.send_response(500)
                    self.send_header("Content-type", ContentType.HTML.value)
                    self.end_headers()
                    self.wfile.write(str(err))
                else:
                    self.send_response(200)
                    content_type = registered_view.content_type.value

                    self.send_header(*registered_view.content_type.to_header())
                    self.end_headers()

                    if content_type == ContentType.JSON:
                        response = json.dumps(response)

                    self.wfile.write(response.encode("utf-8"))
            else:
                self.send_response(404)
                self.send_header("Content-type", ContentType.HTML.value)
                self.end_headers()
                self.wfile.write(b"<h1>404 Not Found</h1>")

    @classmethod
    def set_views(cls, views: Views):
        with cls.__lock:
            if not cls.__views:
                cls.__views = views
        return cls

    @classmethod
    def are_views(cls) -> bool:
        return cls.__views is not None


class RequestHandlerFactory:
    __handler_cls = None
    __lock = Lock()

    @classmethod
    def get_class(cls, views: Views) -> type[RequestHandler]:
        with cls.__lock:
            if cls.__handler_cls and cls.__handler_cls.are_views():
                return cls.__handler_cls
            cls.__handler_cls = RequestHandler.set_views(views)
            return RequestHandler
