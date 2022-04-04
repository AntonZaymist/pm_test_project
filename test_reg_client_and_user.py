from constants import TITLE
from PO.main_page import MainPage


def test_registration_client_and_user(chrome_driver):
    page = MainPage(chrome_driver)
    page.open()
    registration_page = page.open_register_client_and_user_page()
    registration_page.registration_form()
    registration_page_already_registered = page.open_register_client_and_user_page_already_registered()
    registration_page_already_registered.check_registration_form()
    registration_page_already_registered.login_data()
    registration_page_already_registered.password_data()
    assert registration_page_already_registered.login_data() == \
           registration_page_already_registered.login_data()
    assert registration_page_already_registered.password_data() == \
           registration_page_already_registered.password_data()


def test_registration_and_reset_client_and_user(chrome_driver):
    page = MainPage(chrome_driver)
    page.open()
    registration_page = page.open_register_client_and_user_page()
    registration_page.registration_form()
    registration_page_already_registered = page.open_register_client_and_user_page_already_registered()
    registration_page_already_registered.check_registration_form()
    registration_page_already_registered.reset_reg()
    assert registration_page_already_registered.get_title() == TITLE
