import pytest
from selenium.webdriver.support import expected_conditions as EC
from data import URLs, Credentials
from locators import MainPageLocators, LoginFormLocators, RegistrationPageLocators, PasswordRecoveryLocators

class TestLogin:
    """Тесты функциональности входа"""

    def login_user(self, driver, wait, email, password):
        """Метод для входа пользователя"""
        email_input = wait.until(EC.presence_of_element_located(LoginFormLocators.EMAIL_INPUT))
        email_input.send_keys(email)
        password_input = driver.find_element( *LoginFormLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        login_button=wait.until(EC.element_to_be_clickable(LoginFormLocators.LOGIN_BUTTON))
        login_button.click()

    def test_login_via_main_page_button(self, driver, wait):
        """Вход через кнопку 'Войти в аккаунт' на главной странице"""
        driver.get(URLs.MAIN)
        login_account_button = wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_ACCOUNT_BUTTON))
        login_account_button.click()
        self.login_user(driver, wait, Credentials.EMAIL,Credentials.PASSWORD)
        order_button = wait.until(EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert order_button.is_displayed()
        assert driver.current_url == URLs.MAIN

    def test_login_via_personal_account_button(self, driver, wait):
        """Вход через кнопку 'Личный кабинет'"""
        driver.get(URLs.MAIN)
        pesonal_account_button = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        pesonal_account_button.click()
        self.login_user(driver, wait, Credentials.EMAIL, Credentials.PASSWORD)
        wait.until(EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON))
        order_button = wait.until(EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert order_button.is_displayed()
        assert driver.current_url == URLs.MAIN

    def test_login_via_registration_form(self, driver, wait):
        """Вход через кнопку в форме регистрации"""
        driver.get(URLs.REGISTER)
        login_link=wait.until(EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK))
        login_link.click()
        self.login_user(driver, wait, Credentials.EMAIL, Credentials.PASSWORD)
        order_button=wait.until(EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert order_button.is_displayed()
        assert driver.current_url == URLs.MAIN

    def test_login_via_password_recovery_form(self, driver, wait):
        """Вход через кнопку в форме восстановления пароля"""
        driver.get(URLs.FORGOT_PASSWORD)
        login_link=wait.until(EC.element_to_be_clickable(PasswordRecoveryLocators.LOGIN_LINK))
        login_link.click()
        self.login_user(driver, wait, Credentials.EMAIL, Credentials.PASSWORD)
        order_button=wait.until(EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert order_button.is_displayed()
        assert driver.current_url == URLs.MAIN