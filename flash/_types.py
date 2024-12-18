from enum import Enum


class ContentType(str, Enum):
    # call .value to get
    JSON = "application/json"
    HTML = "text/html"
    XML = "application/xml"

    def to_header(self) -> tuple[str, str]:
        return "Content-type", self.value


class HttpMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
