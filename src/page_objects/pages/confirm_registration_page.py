from selenium.webdriver.common.by import By

from src.page_objects.pages.base_page import BasePage


class ConfirmRegistrationPage(BasePage):
    CONFIRMATION_CODE_FIELD = (By.XPATH, '//input[@data-id="confirm-code-input"]')

    def __init__(self, driver):
        super().__init__(driver)

    def fill_in_verification_code(self, verification_code: str):
        self.driver.find_element(*self.CONFIRMATION_CODE_FIELD).send_keys(verification_code)
        return self
