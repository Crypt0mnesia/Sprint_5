import pytest
from selenium.webdriver.support import expected_conditions as EC

from data import URLs, TextMessages
from locators import ConstructorLocators



class TestConstructorSections:
    """Тесты разделов конструктора"""

    def test_switch_to_buns_section(self, driver, wait):
        """Переход к разделу 'Булки'"""
        driver.get(URLs.MAIN)

        sauces_section = wait.until(EC.element_to_be_clickable(ConstructorLocators.SAUCES_SECTION))
        sauces_section.click()

        buns_section = wait.until(EC.element_to_be_clickable(ConstructorLocators.BUNS_SECTION))
        buns_section.click()

        active_section = wait.until(EC.presence_of_element_located(ConstructorLocators.ACTIVE_SECTION))
        assert TextMessages.BUNS in active_section.text

    def test_switch_to_sauces_section(self, driver, wait):
        """Переход к разделу 'Соусы'"""
        driver.get(URLs.MAIN)

        sauces_section = wait.until(EC.element_to_be_clickable(ConstructorLocators.SAUCES_SECTION))
        sauces_section.click()

        active_section = wait.until(EC.presence_of_element_located(ConstructorLocators.ACTIVE_SECTION))
        assert TextMessages.SAUCES in active_section.text

    def test_switch_to_fillings_section(self, driver, wait):
        """Переход к разделу 'Начинки'"""
        driver.get(URLs.MAIN)

        fillings_section = wait.until(EC.element_to_be_clickable(ConstructorLocators.FILLINGS_SECTION))
        fillings_section.click()

        active_section = wait.until(EC.presence_of_element_located(ConstructorLocators.ACTIVE_SECTION))
        assert TextMessages.FILLINGS in active_section.text
