import time
from conftest import driver
from locators import Locators


class TestConstructor:

    def test_constructor_section_fillings(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.BUTTON_FILLING).click()
        assert 'Начинки' in driver.find_element(*Locators.CURRENT_TAB).text

    def test_constructor_section_sauce(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.BUTTON_SAUCE).click()
        assert 'Соусы' in driver.find_element(*Locators.CURRENT_TAB).text

    def test_constructor_section_buns(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.BUTTON_FILLING).click()
        driver.find_element(*Locators.BUTTON_BUN).click()
        assert 'Булки' in driver.find_element(*Locators.CURRENT_TAB).text
