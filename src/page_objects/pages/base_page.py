from selenium.webdriver.common.by import By

from src.browser.browser import browser


class BasePage:
    USER_MENU_BUTTON = (By.XPATH, '//button[@name="user-menu"]')
    LOG_OUT_BUTTON = (By.XPATH, '//button[@data-id="log-out-button"]')

    def __init__(self):
        self.driver = browser.driver

    def open_user_menu(self):
        self.driver.find_element(*self.USER_MENU_BUTTON).click()
        return self

    def log_out(self):
        self.driver.find_element(*self.LOG_OUT_BUTTON).click()
        return self
