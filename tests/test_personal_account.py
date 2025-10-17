import pytest
from selenium.webdriver.support import expected_conditions as EC

from data import URLs
from locators import HeaderLocators, ProfilePageLocators

class TestPersonalAccount:
    """Тест перехода в личный кабинет зарегистрированным пользователем"""
    def test_go_to_personal_account(self, wait, authenticated_user):
        driver = authenticated_user

        pesonal_account_button = wait.until(EC.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_BUTTON))
        pesonal_account_button.click()

        profile_section=wait.until(EC.visibility_of_element_located(ProfilePageLocators.PROFILE_SECTION))
        #
        assert profile_section.is_displayed()
        assert driver.current_url == URLs.PROFILE