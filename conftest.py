import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

@pytest.fixture
def driver():
    service = Service(r"D:\Projects\Sprint_6\geckodriver.exe")  # Укажи свой путь
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    driver = webdriver.Firefox(service=service, options=options)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()
    