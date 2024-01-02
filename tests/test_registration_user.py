from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import Locators
from data_random import DataRandom


class TestRegistration:
    def test_registration_user(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.NAME_FIELD_REGISTRATION).send_keys(DataRandom.name)
        driver.find_element(*Locators.EMAIL_FIELD_REGISTRATION).send_keys(DataRandom.email)
        driver.find_element(*Locators.PASSWORD_FIELD_REGISTRATION).send_keys(DataRandom.password)
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_contains("site/login"))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_registration_password_error(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.NAME_FIELD_REGISTRATION).click()
        driver.find_element(*Locators.NAME_FIELD_REGISTRATION).send_keys(DataRandom.name)
        driver.find_element(*Locators.EMAIL_FIELD_REGISTRATION).send_keys(DataRandom.email)
        driver.find_element(*Locators.PASSWORD_FIELD_REGISTRATION).send_keys(DataRandom.invalid_password)
        driver.find_element(*Locators.REG_BUTTON).click()
        assert driver.find_element(*Locators.ERROR_REGISTRATION_MESSAGE).text == "Некорректный пароль"
