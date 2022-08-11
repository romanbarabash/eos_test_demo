from time import sleep

import pytest
from selenium.webdriver import Keys, ActionChains

from src.gmail_service.mail_message import MailMessage, MailBodyParser
from src.models.user_model import UserModel


@pytest.fixture
def get_user():
    return UserModel.create()


@pytest.fixture
def user_registration(get_driver, get_user):
    driver = get_driver
    user = get_user
    driver.get("https://crop-monitoring.eos.com/")

    # registration/sign in form
    first_name_field = driver.find_element(by="xpath", value="//input[@formcontrolname='first_name']")
    last_name_field = driver.find_element(by="xpath", value="//input[@formcontrolname='last_name']")
    email_name_field = driver.find_element(by="xpath", value="//input[@formcontrolname='email']")
    password_name_field = driver.find_element(by="xpath", value="//input[@formcontrolname='password']")

    terms_of_use_checkbox = driver.find_element(by="xpath", value="//span[./input[@id='mat-checkbox-1-input']]")
    sign_up_button = driver.find_element(by="xpath", value="//button[@data-id='sign-up-btn']")

    # sign_in_button = driver.find_element(by="xpath", value="//button[@data-id='sign-in-btn']")
    # sign_in_form_button = driver.find_element(by="xpath", value="//button[@data-id='sign-in-button']")
    # sign_up_form_button = driver.find_element(by="xpath", value="//button[@data-id='go-signup-btn']")

    first_name_field.send_keys(user.first_name)
    last_name_field.send_keys(user.last_name)
    email_name_field.send_keys(user.email)
    password_name_field.send_keys(user.password)
    terms_of_use_checkbox.click()

    sign_up_button.send_keys(Keys.END)
    action = ActionChains(driver)
    sleep(3)
    action.move_to_element(sign_up_button).click().perform()

    # get email
    mail = MailMessage()
    messages = mail.get_mime_messages_by_field('to', user.email)
    message_payload = messages[0].get_payload()[0]
    verification_code = MailBodyParser(message_payload).get_mail_verification_code()

    # confirmation code field
    confirmation_code_field = driver.find_element(by="xpath", value="//input[@data-id='confirm-code-input']")
    confirm_email_button = driver.find_element(by="xpath", value="//button[@data-id='submit-code-btn']")

    confirmation_code_field.send_keys(verification_code)
    # confirm_email_button.click()


@pytest.fixture
def log_out(get_driver, get_user):
    driver = get_driver
    close_modal_button = driver.find_element(by="xpath", value="//button[@id='x-button']")
    close_modal_button.click()

    user_menu = driver.find_element(by="xpath", value="//button[@name='user-menu']")
    user_menu.click()

    log_out_button = driver.find_element(by="xpath", value="//button[@data-id='log-out-button']")
    log_out_button.click()
