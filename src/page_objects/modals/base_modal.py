from selenium.webdriver.common.by import By


class BaseModal:
    X_BUTTON = (By.XPATH, "//button[@id='x-button']")

    def __init__(self, get_driver):
        self.driver = get_driver

    def close_popup(self):
        self.driver.find_element(*self.X_BUTTON).click()
        return self
