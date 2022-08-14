import warnings

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

from src.utils.custom_selenium_actions import CustomSeleniumActions


class BaseModal:
    MODAL_ROOT_xpath = "//div[contains(@id, 'cdk-overlay')]"
    X_BUTTON = (By.XPATH, MODAL_ROOT_xpath + "//button[@class='icon small'] | //button[@id='x-button']")

    def __init__(self, get_driver):
        self.driver = get_driver
        self.custom_actions = CustomSeleniumActions(self.driver)

    def close_all_modals(self):
        self.custom_actions.wait_till_element_located_appears(locator=(By.XPATH, self.MODAL_ROOT_xpath))
        for close_icon in self.driver.find_elements(*self.X_BUTTON):
            try:
                self.custom_actions.click_element_using_js(close_icon)
            except StaleElementReferenceException:
                warnings.warn("There are no notification toast messages displayed. Nothing to close")
