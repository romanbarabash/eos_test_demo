import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from config import TIMEOUT
from src.page_objects.modals.base_modal import BaseModal
from src.page_objects.modals.get_gift_modal import GetGiftModal
from src.page_objects.pages.base_page import BasePage
from src.page_objects.pages.confirm_registration_page import ConfirmRegistrationPage
from src.page_objects.pages.sign_up_page import SignUpPage


# region driver setup
@pytest.fixture
def get_driver(get_options) -> WebDriver:
    init_webdriver = webdriver.Chrome(ChromeDriverManager().install(), options=get_options)
    init_webdriver.implicitly_wait(TIMEOUT)
    return init_webdriver


@pytest.fixture
def get_options():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    return options


@pytest.fixture
def close_browser(get_driver):
    yield
    get_driver.quit()


# endregion driver setup

# region pages init

@pytest.fixture
def base_page(get_driver) -> BasePage:
    return BasePage(get_driver)


@pytest.fixture
def sign_up_page(get_driver) -> SignUpPage:
    return SignUpPage(get_driver)


@pytest.fixture
def confirm_registration_page(get_driver) -> ConfirmRegistrationPage:
    return ConfirmRegistrationPage(get_driver)


# endregion pages init

# region modals init
@pytest.fixture
def base_modal(get_driver) -> BaseModal:
    return BaseModal(get_driver)


@pytest.fixture
def get_gift_modal(get_driver) -> GetGiftModal:
    return GetGiftModal(get_driver)

# endregion modals init
