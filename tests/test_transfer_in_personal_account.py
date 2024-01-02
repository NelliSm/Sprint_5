from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from constants import Constants
from locators import Locators


class TestPersonalAccount:
    def test_transition_authorized_user_personal_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_AUTHORISATION).send_keys(Constants.LOGIN_EMAIL)
        driver.find_element(*Locators.PASSWORD_AUTHORISATION).send_keys(Constants.LOGIN_PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
