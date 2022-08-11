import pytest

from src.browser.browser import Browser
from src.page_objects.modals.get_gift_modal import GetGiftModal
from src.page_objects.pages.base_page import BasePage
from src.page_objects.pages.sign_up_page import SignUpPage


# region pages

@pytest.fixture
def base_page() -> BasePage:
    return BasePage()


@pytest.fixture
def sign_up_page() -> SignUpPage:
    return SignUpPage()


# endregion pages

# region modals
@pytest.fixture
def get_gift_modal() -> GetGiftModal:
    return GetGiftModal()


# endregion modals


@pytest.fixture
def get_driver():
    return  Browser().driver


@pytest.fixture
def open_browser(get_driver):
    get_driver.get("https://crop-monitoring.eos.com/")
    yield
    get_driver.quit()
