import logging

import pytest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"

logger = logging.getLogger("cars_api")
logger.setLevel(logging.INFO)
if not logger.handlers:
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    file_handler = logging.FileHandler("test_search.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


@pytest.fixture(scope="class")
def session():
    s = requests.Session()
    response = s.post(f"{BASE_URL}/auth", auth=HTTPBasicAuth("test_user", "test_pass"))
    access_token = response.json()["access_token"]
    s.headers.update({"Authorization": "Bearer " + access_token})
    logger.info("Аутентифікація успішна, токен отримано")
    return s


class TestCarsSearch:
    @pytest.mark.parametrize(
        "sort_by, limit",
        [
            ("price", 5),
            ("year", 10),
            ("engine_volume", 3),
            ("brand", 7),
            ("price", 1),
            ("year", 25),
            ("price", 15),
        ],
    )
    def test_search(self, session, sort_by, limit):
        params = {"sort_by": sort_by, "limit": limit}
        response = session.get(f"{BASE_URL}/cars", params=params)
        logger.info(f"GET /cars sort_by={sort_by} limit={limit} -> {response.status_code}")

        assert response.status_code == 200

        cars = response.json()
        assert isinstance(cars, list)
        assert len(cars) == limit

        values = [car[sort_by] for car in cars]
        assert values == sorted(values)
        logger.info(f"OK: повернуто {len(cars)} авто, відсортованих за '{sort_by}'")
