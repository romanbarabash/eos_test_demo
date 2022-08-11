import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def get_options():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("incognito")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    return options


@pytest.fixture
def get_driver(get_options):
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=get_options)
    driver.implicitly_wait(10)
    return driver


@pytest.fixture
def open_browser(get_driver):
    driver = get_driver
    yield
    driver.quit()

