from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from constants import ConstantsData
from constants import ConstantsUrl
from locators import Locators

#Добавлена проверка авторизации пользователя по наличию кнопки "Выйти" в Личном кабинете

class TestAuthorisation:

    def test_authorisation_user_button_enter_account(self, driver):
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
        assert 'Выход' in driver.find_element(*Locators.BUTTON_EXIT).text

    def test_authorisation_user_button_personal_account(self, driver):
        driver.get(ConstantsUrl.URL)
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_AUTHORISATION).send_keys(ConstantsData.LOGIN_EMAIL)
        driver.find_element(*Locators.PASSWORD_AUTHORISATION).send_keys(ConstantsData.LOGIN_PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(ConstantsUrl.URL))
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(ConstantsUrl.URL_PROFILE))
        assert 'Выход' in driver.find_element(*Locators.BUTTON_EXIT).text

    def test_authorisation_user_button_link_login_form(self, driver):
        driver.get(ConstantsUrl.URL_REG)
        driver.find_element(*Locators.BUTTON_LINK_LOGIN).click()
        driver.find_element(*Locators.EMAIL_AUTHORISATION).send_keys(ConstantsData.LOGIN_EMAIL)
        driver.find_element(*Locators.PASSWORD_AUTHORISATION).send_keys(ConstantsData.LOGIN_PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(ConstantsUrl.URL))
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(ConstantsUrl.URL_PROFILE))
        assert 'Выход' in driver.find_element(*Locators.BUTTON_EXIT).text

    def test_authorisation_user_button_password_recovery_form(self, driver):
        driver.get(ConstantsUrl.URL_RECOVER)
        driver.find_element(*Locators.BUTTON_LINK_LOGIN).click()
        driver.find_element(*Locators.EMAIL_AUTHORISATION).send_keys(ConstantsData.LOGIN_EMAIL)
        driver.find_element(*Locators.PASSWORD_AUTHORISATION).send_keys(ConstantsData.LOGIN_PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(ConstantsUrl.URL))
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(ConstantsUrl.URL_PROFILE))
        assert 'Выход' in driver.find_element(*Locators.BUTTON_EXIT).text
