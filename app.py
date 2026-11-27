"""Простое веб-приложение на Flask."""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """Главная страница."""
    return "Hello, world!"


if __name__ == "__main__":
    app.run(debug=True)
