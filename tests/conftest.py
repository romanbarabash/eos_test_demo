import pytest

from src.gmail_service.mail_message import MailMessage, MailBodyParser
from src.models.user_model import UserModel


@pytest.fixture
def get_user():
    return UserModel.create()


@pytest.fixture
def user_registration(sign_up_page, get_driver, get_user):
    driver = get_driver
    user = get_user

    sign_up_page \
        .sign_up(user=get_user)

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
def log_out(base_page, get_gift_modal, get_driver, get_user):
    get_gift_modal \
        .close_popup()

    base_page \
        .open_user_menu() \
        .log_out()
