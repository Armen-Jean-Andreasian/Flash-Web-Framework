# Flash Web Framework

A lightweight web framework, similar to Flask or Bottle, designed to demonstrate how to build your own web framework. 


---
## Example Usage

This example demonstrates how to create routes, handle HTTP methods, and serve content using the `FlashFramework`.


```python
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
```

---
## License

- Author: Armen-Jean Andreasian
- License: MIT
