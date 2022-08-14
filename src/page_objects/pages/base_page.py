from urllib.parse import urljoin

from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By

from src.models.user_model import UserModel
from src.utils.custom_selenium_actions import CustomSeleniumActions


class BasePage():
    USER_MENU_BUTTON_xpath = '//button[@name="user-menu"]'
    USER_MANU_NAME_xpath = USER_MENU_BUTTON_xpath + '//div[@class="full-user-name"]'
    LOG_OUT_BUTTON = (By.XPATH, '//button[@data-id="log-out-button"]')
    LOAD_SPINNER = (By.XPATH, '//div[@data-id="global-layers-loader"]')

    def __init__(self, driver):
        self.driver = driver
        self.custom_actions = CustomSeleniumActions(self.driver)

    def wait_for_page_loaded(self):
        self.custom_actions.wait_till_element_located_appears(locator=self.LOAD_SPINNER)
        self.custom_actions.wait_till_element_located_disappear(locator=self.LOAD_SPINNER)
        return self

    def open_url(self, url: str):
        self.driver.get(url)
        return self

    def _join_url(self, host: str, path: str):
        return urljoin(host, path)

    def open_user_menu(self):
        self.custom_actions.wait_till_element_located_appears(locator=(By.XPATH, self.USER_MENU_BUTTON_xpath))
        self.driver.find_element(By.XPATH, self.USER_MENU_BUTTON_xpath).click()
        return self

    def verify_user_menu_account(self, user: UserModel):
        account_name = self.driver.find_element(By.XPATH, self.USER_MANU_NAME_xpath).text
        assert_that(account_name, equal_to(f'{user.first_name} {user.last_name}'))
        return self

    def log_out(self):
        self.custom_actions.wait_till_element_located_appears(locator=self.LOG_OUT_BUTTON)
        self.custom_actions.click_element_using_actions(self.driver.find_element(*self.LOG_OUT_BUTTON))
        self.custom_actions.wait_till_element_located_disappear(locator=self.LOG_OUT_BUTTON)
        return self
