import pytest
from selenium import webdriver
from constants import BASE_URL


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=options)  # Без Service
    driver.get(BASE_URL)
    yield driver
    driver.quit()