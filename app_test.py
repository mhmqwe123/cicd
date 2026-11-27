import unittest
from app import app


class TestApp(unittest.TestCase):
    """Набор unit-тестов для Flask-приложения."""

    def setUp(self):
        """Создаём тестовый клиент перед каждым тестом."""
        self.client = app.test_client()

    def test_home(self):
        """Проверяем, что корневой URL возвращает 'Hello, world!'."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data().decode(), "Hello, world!")

    def test_health(self):
        """Проверяем, что /health возвращает статус ok."""
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_version(self):
        """Проверяем, что /version возвращает корректную версию."""
        response = self.client.get("/version")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"version": "1.0.0"})

    def test_sum(self):
        """Проверяем сложение двух чисел."""
        response = self.client.get("/sum/3/4")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"result": 7})

    def test_sum_negative(self):
        """Проверяем сложение с отрицательным числом."""
        response = self.client.get("/sum/-5/2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"result": -3})

    def test_not_found(self):
        """Проверяем, что несуществующий маршрут возвращает 404."""
        response = self.client.get("/nonexistent")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
