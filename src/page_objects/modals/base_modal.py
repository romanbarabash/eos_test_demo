from selenium.webdriver.common.by import By

from src.browser.browser import browser


class BaseModal:
    X_BUTTON = (By.XPATH, "//button[@id='x-button']")

    def __init__(self):
        self.driver = browser.driver

    def close_popup(self):
        self.driver.find_element(*self.X_BUTTON).click()
        return self
