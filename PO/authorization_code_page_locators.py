from selenium.webdriver.common.by import By


class AuthorizationCodePageLocators:
    AUTHORIZE_BUTTON = (By.XPATH, "//a[@class='button is-primary auth-url']")
    REGISTER_A_CLIENT_BUTTON = (By.XPATH, "//a[@class='button is-primary' and text()='Register a Client']")
    REGISTER_BUTTON = (By.XPATH, "//*[@class='register-new is-primary button']")
    STATE_PARAMETER = (By.XPATH, "//span[@class='oauth2-state']")
    USERNAME_LOG_IN = (By.XPATH, "//*[@id='username']")
    PASSWORD_LOG_IN = (By.XPATH, "//*[@id='password']")
    LOG_IN_BUTTON = (By.XPATH, "//*[@id='log-in-button']")
    APPROVE_BUTTON = (By.XPATH, "//*[@id='redirect-uri']")
    LOGIN_DATA = (By.XPATH, "//*[@class='user-login']")
    PASSWORD_DATA = (By.XPATH, "//*[@class='user-password']")
    CONTINUE_BUTTON = (By.XPATH, "//*[@class='continue is-primary button']")
