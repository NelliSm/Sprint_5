from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from constants import ConstantsData
from constants import ConstantsUrl
from locators import Locators


class TestTransfer:
    def test_transition_authorized_user_from_personal_account_in_constructor(self, driver):
        driver.get(ConstantsUrl.URL)
        driver.find_element(*Locators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_AUTHORISATION).send_keys(ConstantsData.LOGIN_EMAIL)
        driver.find_element(*Locators.PASSWORD_AUTHORISATION).send_keys(ConstantsData.LOGIN_PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(ConstantsUrl.URL))
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(ConstantsUrl.URL_PROFILE))
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(ConstantsUrl.URL))
        assert driver.current_url == ConstantsUrl.URL

    def test_clicking_logo_button_from_personal_account(self, driver):
        driver.get(ConstantsUrl.URL)
        driver.find_element(*Locators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_AUTHORISATION).send_keys(ConstantsData.LOGIN_EMAIL)
        driver.find_element(*Locators.PASSWORD_AUTHORISATION).send_keys(ConstantsData.LOGIN_PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(ConstantsUrl.URL))
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(ConstantsUrl.URL_PROFILE))
        driver.find_element(*Locators.BUTTON_LOGO_EMAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(ConstantsUrl.URL))
        assert driver.current_url == ConstantsUrl.URL
