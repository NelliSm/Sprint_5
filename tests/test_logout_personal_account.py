from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from constants import ConstantsUrl
from constants import ConstantsData
from locators import Locators


class TestLogout:
    def test_logout_from_personal_account(self, driver):
        driver.get(ConstantsUrl.URL)
        driver.find_element(*Locators.BUTTON_ENTER_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_AUTHORISATION).send_keys(ConstantsData.LOGIN_EMAIL)
        driver.find_element(*Locators.PASSWORD_AUTHORISATION).send_keys(ConstantsData.LOGIN_PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(ConstantsUrl.URL))
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(ConstantsUrl.URL_PROFILE))
        driver.find_element(*Locators.BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(ConstantsUrl.URL_LOGIN))
        assert driver.current_url == ConstantsUrl.URL_LOGIN
