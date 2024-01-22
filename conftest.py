import pytest
from selenium import webdriver


# Фикстура создания экземпляра для браузера. Закрывает браузер после каждого теста
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
