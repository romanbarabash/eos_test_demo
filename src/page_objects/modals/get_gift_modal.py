from selenium.webdriver.common.by import By

from src.page_objects.modals.base_modal import BaseModal


class GetGiftModal(BaseModal):
    MODAL_ROOT_xpath = "//div[contains(@id, 'cdk-overlay')]"
    BUSINESS_TYPE_SELECT = (By.XPATH, MODAL_ROOT_xpath + "//*[@data-id='gift-business-dropdown']")
    BUSINESS_TYPE_ITEM_xpath = "//span[contains(text(),'{}')]"
    TOTAL_AREA_INPUT = (By.XPATH, MODAL_ROOT_xpath + "//input[@id='total-area']")
    GET_YOUR_GIFT_BUTTON = (By.XPATH, MODAL_ROOT_xpath + "//button[@id='submit-button']")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_gift_form(self, business_type: str, field_area: int):
        self.driver.find_element(*self.BUSINESS_TYPE_SELECT).click()
        self.driver.find_element(By.XPATH, self.BUSINESS_TYPE_ITEM_xpath.format(business_type)).click()
        self.driver.find_element(*self.TOTAL_AREA_INPUT).send_keys(field_area)
        self.driver.find_element(*self.GET_YOUR_GIFT_BUTTON).click()
        return self
