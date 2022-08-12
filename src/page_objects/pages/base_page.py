from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By

from src.browser.browser import browser
from src.models.user_model import UserModel


class BasePage:
    USER_MENU_BUTTON_xpath = '//button[@name="user-menu"]'
    USER_MANU_NAME_xpath = USER_MENU_BUTTON_xpath + '//div[@class="full-user-name"]'
    LOG_OUT_BUTTON = (By.XPATH, '//button[@data-id="log-out-button"]')

    def __init__(self):
        self.driver = browser.driver

    def open_user_menu(self):
        self.driver.find_element(By.XPATH, self.USER_MENU_BUTTON_xpath).click()
        return self

    def verify_user_menu_account(self, user: UserModel):
        account_name = self.driver.find_element(By.XPATH, self.USER_MANU_NAME_xpath).text
        assert_that(account_name, equal_to(f'{user.first_name} {user.last_name}'))
        return self

    def log_out(self):
        self.driver.find_element(*self.LOG_OUT_BUTTON).click()
        return self
