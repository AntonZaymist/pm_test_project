from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    REGISTER_BUTTON = (By.XPATH, "//*[@class='register-new is-primary button']")
    CONTINUE_BUTTON_REGISTRATION_FORM = (By.XPATH, "//*[@class='continue is-primary button']")
    BACK_TO_FLOWS_BUTTON = (By.XPATH, "//*[@href='index.html']")
    RESET_BUTTON_REGISTRATION_FORM = (By.XPATH, "//*[@class='reset-session is-danger button']")
    VIEW_REGISTRATION_INFO_BUTTON = (
        By.XPATH,
        "//a[@class='view-registration is-primary button' and text()='View Registration Info']")
    USER_LOGIN_REGISTRATION_FORM = (By.XPATH, "//*[@class='user-login']")
    USER_PASSWORD_REGISTRATION_FORM = (By.XPATH, "//*[@class='user-password']")
    CLOSE_BUTTON_REGISTRATION_FORM = (By.XPATH, "//*[@class='close button']")
