from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    """Корневой маршрут — возвращает приветствие."""
    return "Hello, world!"


@app.route("/health")
def health():
    """Проверка работоспособности сервиса (для CI/CD и мониторинга)."""
    return jsonify({"status": "ok"})


@app.route("/version")
def version():
    """Возвращает текущую версию приложения."""
    return jsonify({"version": "1.0.0"})


@app.route("/sum/<int:a>/<int:b>")
def sum_numbers(a: int, b: int):
    """Пример бизнес-логики: сложение двух чисел."""
    return jsonify({"result": a + b})


if __name__ == "__main__":
    app.run(debug=True)
