# conftest.py
import logging
import pytest


def setup_logging():
    log_format = "PYTEST %(levelname)s [%(asctime)s] - %(name)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_format)


@pytest.fixture(scope="session", autouse=True)
def setup_logging_fixture():
    setup_logging()
