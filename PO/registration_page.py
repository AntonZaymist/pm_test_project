from PO.base_page import BasePage
from PO.registration_page_locators import RegistrationPageLocators


class RegisterPage(BasePage):
    # def get_register_form(self):
    #     return self.find_element(RegistrationPageLocators.REGISTER_BUTTON)
    #
    # def open_client_registration(self):
    #     return self.find_element(RegistrationPageLocators.CONTINUE_BUTTON_REGISTRATION_FORM)

    def get_title(self):
        return self.chrome_driver.title

    def registration_form(self):
        open_register = self.find_element(RegistrationPageLocators.REGISTER_BUTTON)
        open_register.click()
        continue_register_form = self.find_element(RegistrationPageLocators.CONTINUE_BUTTON_REGISTRATION_FORM)
        continue_register_form.click()

    def check_registration_form(self):
        view_reg_info = self.find_element(RegistrationPageLocators.VIEW_REGISTRATION_INFO_BUTTON)
        view_reg_info.click()

    def login_data(self):
        return self.find_element(RegistrationPageLocators.USER_LOGIN_REGISTRATION_FORM).text

    def password_data(self):
        return self.find_element(RegistrationPageLocators.USER_PASSWORD_REGISTRATION_FORM).text

    def reset_reg(self):
        reset_registration = self.find_element(RegistrationPageLocators.RESET_BUTTON_REGISTRATION_FORM)
        reset_registration.click()

    def back_to_flows(self):
        close_button = self.find_element(RegistrationPageLocators.CLOSE_BUTTON_REGISTRATION_FORM)
        close_button.click()
        back_to_flows = self.find_element(RegistrationPageLocators.BACK_TO_FLOWS_BUTTON)
        back_to_flows.click()





