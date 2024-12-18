import http.server
import socketserver
from typing import Callable, Any
import json
from view_keeper import ViewKeeper
from _types import ContentType, HttpMethod

VIEW_KEEPER = ViewKeeper()


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if registered_view := VIEW_KEEPER.get(self.path):
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


class FlashFramework:
    def run(self, host: str, port: str | int):
        self._register_info_page()
        with socketserver.TCPServer((host, port), RequestHandler) as httpd:
            print(f"Server started at http://{host}:{port}")

            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("Server Stopped")

    def route(self, path: str, content_type: ContentType, method: HttpMethod = 'GET') -> Callable:
        def inner(func: Callable):
            if path not in VIEW_KEEPER:
                VIEW_KEEPER.add_view(
                    path=path,
                    content_type=content_type,
                    http_method=method,
                    callback=func
                )
            return func

        return inner

    def _register_info_page(self):
        """Hardcoded /info path to provide info on app"""
        VIEW_KEEPER.add_view(
            path='/info',
            content_type=ContentType.JSON,
            http_method=HttpMethod.GET,
            callback=lambda: VIEW_KEEPER.registered_paths
        )
