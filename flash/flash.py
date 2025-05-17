import socketserver
from typing import Callable
from flash.components.views import Views
from flash.components.handlers import RequestHandlerFactory
from flash.types import ContentType, HttpMethod

VIEWS = Views()

RequestHandler = RequestHandlerFactory.get_class(views=VIEWS)


def register_info_page():
    """Hardcoded /info path to provide info on app"""
    VIEWS.add_view(
        path='/info',
        content_type=ContentType.JSON,
        http_method=HttpMethod.GET,
        callback=lambda: VIEWS.registered_paths
    )


class Flash:
    def __init__(self, info_path=True):
        self.scheme = None
        self.host = None
        self.port = None

        if info_path:
            register_info_page()

    def __post_init__(self, scheme, host, port):
        self.scheme = scheme
        self.host = host
        self.port = port

    def _todo_serve_https(self, host, port, *args, **kwargs):
        self.__post_init__(scheme='https', host=host, port=port)
        ...
        raise RuntimeError("HTTPS is not supported yet.")

    def _serve_http(self, host, port):
        self.__post_init__(scheme='http', host=host, port=port)

        with socketserver.TCPServer((self.host, self.port), RequestHandler) as httpd:
            print(f"Server started at http://{self.host}:{self.port}")
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("Server Stopped")

    def run(self, host: str, port: str | int, https=False):
        return self._todo_serve_https() if https else self._serve_http(host, port)

    def route(self, path: str, content_type: ContentType, method: HttpMethod = 'GET') -> Callable:
        def register_route(func: Callable):
            if path not in VIEWS:
                VIEWS.add_view(
                    path=path,
                    content_type=content_type,
                    http_method=method,
                    callback=func,
                )
            return func

        return register_route

    @property
    def running_on(self) -> str:
        return f"{self.scheme}://{self.host}:{self.port}"
