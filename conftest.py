import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope="session")
def chrome_driver():
    chrome_driver = Chrome()
    chrome_driver.implicitly_wait(15)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()
