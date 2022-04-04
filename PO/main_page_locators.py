from selenium.webdriver.common.by import By


class MainPageLocators:
    AUTHORIZATION_CODE_REGISTRATION = (By.XPATH, "//*[@href='authorization-code.html']")
    CLIENT_AND_USER_REGISTRATION = (
        By.XPATH, "//a[@href='client-registration.html' and text()='register a client and a user']")
    CLIENT_AND_USER_REGISTRATION_ALREADY_REGISTERED = (
        By.XPATH, "//a[@href='client-registration.html' and text()='client and user registration']")
