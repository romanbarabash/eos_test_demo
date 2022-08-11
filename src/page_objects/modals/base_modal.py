from selenium.webdriver.common.by import By

from src.browser.browser import Browser


class BaseModal:
    MODAL_ROOT = (By.XPATH, "//div[@id='cdk-overlay-0']")
    X_BUTTON = (By.XPATH, "//button[@id='x-button']")


    def __init__(self):
        self.driver = Browser().driver

    def close_popup(self):
        self.driver.find_element(*self.X_BUTTON).click()
        return self

    def _get_popup(self):
        elements = self.driver.find_elements(*self.MODAL_ROOT)
        if len(elements) > 1:
            elements.pop()
        return elements.pop()
