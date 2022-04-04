from PO.main_page import MainPage


def test_registration_client_and_user(chrome_driver):
    page = MainPage(chrome_driver)
    page.open()
    authorize_page = page.open_authorization_code()
    authorize_page.authorize_step()
    authorize_page.login_data()
    authorize_page.password_data()
    authorize_page.continue_button()
    authorize_page.state_parameter()
    authorize_page.authorize_button()
    authorize_page.username_input().send_keys(authorize_page.login_data())
