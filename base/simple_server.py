import http.server
import socketserver

HOST = "0.0.0.0"
PORT = 8080


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello, World! </h1>")


with socketserver.TCPServer((HOST, PORT), RequestHandler) as httpd:
    print(f"Server started at http://{HOST}:{PORT}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server Stopped")
