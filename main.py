import random
from flash import FlashFramework
from flash import HttpMethod, ContentType

app = FlashFramework()


@app.route(path="/", content_type=ContentType.HTML, method=HttpMethod.GET)
def home():
    return "<h1>Welcome to FlashFramework!</h1>"


@app.route("/about", content_type=ContentType.HTML, method=HttpMethod.GET)
def about():
    return "<h1>About Page</h1>"


@app.route("/hello", content_type=ContentType.HTML, method=HttpMethod.GET)
def hello():
    return "<h1>Hello, World!</h1>"


@app.route(path='/data', content_type=ContentType.JSON, method=HttpMethod.GET)
def data():
    return {random.randint(1, 100): random.randint(1, 200)}


if __name__ == "__main__":
    app.run("127.0.0.1", 8080)
