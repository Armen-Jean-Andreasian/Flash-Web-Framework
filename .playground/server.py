import random
from flash import Flash
from flash import HttpMethod, ContentType
from flash import render_html, render_json

app = Flash()


@app.route(path="/", content_type=ContentType.HTML, method=HttpMethod.GET)
def home():
    return f"<h1>Welcome to Flash!</h1> <br> Visit {app.running_on + '/info'} to see available paths"


@app.route("/about", content_type=ContentType.HTML, method=HttpMethod.GET)
def about():
    return "<h1>About Page</h1>"


@app.route("/hello", content_type=ContentType.HTML, method=HttpMethod.GET)
def hello():
    return "<h1>Hello, World!</h1>"


@app.route(path='/data', content_type=ContentType.JSON, method=HttpMethod.GET)
def data():
    return {random.randint(1, 100): random.randint(1, 200)}


@app.route(path='/some_html', content_type=ContentType.HTML, method=HttpMethod.GET)
def my_html():
    return render_html('templates/asd.html')


@app.route(path='/some_json', content_type=ContentType.JSON, method=HttpMethod.GET)
def my_json():
    return render_json('files/file.json')


if __name__ == "__main__":
    app.run("127.0.0.1", 8080)
