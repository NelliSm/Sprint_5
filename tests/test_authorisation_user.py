from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from constants import Constants
from locators import Locators


class TestAuthorisation:

    def test_authorisation_user_button_enter_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_AUTHORISATION).send_keys(Constants.LOGIN_EMAIL)
        driver.find_element(*Locators.PASSWORD_AUTHORISATION).send_keys(Constants.LOGIN_PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_authorisation_user_button_personal_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_AUTHORISATION).send_keys(Constants.LOGIN_EMAIL)
        driver.find_element(*Locators.PASSWORD_AUTHORISATION).send_keys(Constants.LOGIN_PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_authorisation_user_button_link_login_form(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.BUTTON_LINK_LOGIN).click()
        driver.find_element(*Locators.EMAIL_AUTHORISATION).send_keys(Constants.LOGIN_EMAIL)
        driver.find_element(*Locators.PASSWORD_AUTHORISATION).send_keys(Constants.LOGIN_PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_authorisation_user_button_password_recovery_form(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        driver.find_element(*Locators.BUTTON_LINK_LOGIN).click()
        driver.find_element(*Locators.EMAIL_AUTHORISATION).send_keys(Constants.LOGIN_EMAIL)
        driver.find_element(*Locators.PASSWORD_AUTHORISATION).send_keys(Constants.LOGIN_PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
