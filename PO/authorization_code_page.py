from PO.base_page import BasePage
from PO.authorization_code_page_locators import AuthorizationCodePageLocators


class AuthorizationCodePage(BasePage):

    def authorize_step(self):
        register_a_client_button = self.find_element(AuthorizationCodePageLocators.REGISTER_A_CLIENT_BUTTON)
        register_a_client_button.click()
        register_client = self.find_element(AuthorizationCodePageLocators.REGISTER_BUTTON)
        register_client.click()
        # authorize_button = self.find_element(AuthorizationCodePageLocators.AUTHORIZE_BUTTON)
        # authorize_button.click()

    def login_data(self):
        return self.find_element(AuthorizationCodePageLocators.LOGIN_DATA).text

    def password_data(self):
        return self.find_element(AuthorizationCodePageLocators.PASSWORD_DATA).text

    def continue_button(self):
        continue_button_use = self.find_element(AuthorizationCodePageLocators.CONTINUE_BUTTON)
        continue_button_use.click()

    def state_parameter(self):
        return self.find_element(AuthorizationCodePageLocators.STATE_PARAMETER).text

    def authorize_button(self):
        authorize_button_click = self.find_element(AuthorizationCodePageLocators.AUTHORIZE_BUTTON)
        authorize_button_click.click()

    def username_input(self):
        return self.find_element(AuthorizationCodePageLocators.USERNAME_LOG_IN)

    def password_input(self):
        return self.find_element(AuthorizationCodePageLocators.PASSWORD_LOG_IN)

    def log_in_input(self):
        return self.find_element(AuthorizationCodePageLocators.LOG_IN_BUTTON)
