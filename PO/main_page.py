from PO.authorization_code_page import AuthorizationCodePage
from PO.base_page import BasePage
from PO.main_page_locators import MainPageLocators
from PO.registration_page import RegisterPage


class MainPage(BasePage):
    URL = 'https://www.oauth.com/playground/index.html'

    def __init__(self, chrome_driver):
        super().__init__(chrome_driver, self.URL)

    def open_register_client_and_user_page(self):
        login_link = self.find_element(MainPageLocators.CLIENT_AND_USER_REGISTRATION)
        login_link.click()
        return RegisterPage(self.chrome_driver, self.chrome_driver.current_url)

    def open_register_client_and_user_page_already_registered(self):
        login_link_already_registered = self.find_element(
            MainPageLocators.CLIENT_AND_USER_REGISTRATION_ALREADY_REGISTERED)
        login_link_already_registered.click()
        return RegisterPage(self.chrome_driver, self.chrome_driver.current_url)

    def open_authorization_code(self):
        login_link = self.find_element(MainPageLocators.AUTHORIZATION_CODE_REGISTRATION)
        login_link.click()
        return AuthorizationCodePage(self.chrome_driver, self.chrome_driver.current_url)
