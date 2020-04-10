from app import create_app
from config import Config

app = create_app(Config)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
