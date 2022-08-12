from time import sleep

from selenium.webdriver.common.by import By

from src.models.user_model import UserModel
from src.page_objects.pages.base_page import BasePage


class SignUpPage(BasePage):
    FIRST_NAME_FIELD = (By.XPATH, '//input[@formcontrolname="first_name"]')
    LAST_NAME_FIELD = (By.XPATH, '//input[@formcontrolname="last_name"]')
    EMAIL_FIELD = (By.XPATH, '//input[@formcontrolname="email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@formcontrolname="password"]')
    TERMS_OF_USE_CHECKBOX = (By.XPATH, '//span[./input[@id="mat-checkbox-1-input"]]')
    SIGN_UP_BUTTON = (By.XPATH, '//button[@data-id="sign-up-btn"]')
    SIGN_IN_BUTTON = (By.XPATH, '//button[@data-id="sign-in-btn"]')
    SIGN_IN_FORM_BUTTON = (By.XPATH, '//button[@data-id="sign-in-button"]')

    def __init__(self):
        super().__init__()

    def sign_up(self, user: UserModel):
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(user.first_name)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(user.last_name)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(user.email)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(user.password)
        self.driver.find_element(*self.TERMS_OF_USE_CHECKBOX).click()
        sign_up_button = self.driver.find_element(*self.SIGN_UP_BUTTON)
        sleep(2)  # TODO - add flexible wait here
        sign_up_button.click()
        return self

    def sign_in(self, user: UserModel):
        self.driver.find_element(*self.SIGN_IN_FORM_BUTTON).click()
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(user.email)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(user.password)
        self.driver.find_element(*self.SIGN_IN_BUTTON).click()
        return self
