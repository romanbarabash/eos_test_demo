import pytest

from src.gmail_service.mail_message import MailMessage, MailBodyParser
from src.models.user_model import UserModel


@pytest.fixture
def get_user():
    return UserModel.create()


@pytest.fixture
def user_registration(sign_up_page, get_user):
    sign_up_page \
        .open_page() \
        .sign_up(user=get_user)


@pytest.fixture
def get_email_verification_code(get_user):
    mail = MailMessage()
    messages = mail.get_mime_messages_by_field('to', get_user.email)
    message_payload = messages[0].get_payload()[0]
    return MailBodyParser(message_payload).get_mail_verification_code()


@pytest.fixture
def confirm_registration(confirm_registration_page, get_email_verification_code):
    confirm_registration_page \
        .fill_in_verification_code(get_email_verification_code)


@pytest.fixture
def log_out(base_page, get_gift_modal, get_user):
    base_page \
        .wait_for_page_loaded()

    get_gift_modal \
        .close_popup()  # TODO - randomly fails on this step, modal does not have 'x' icon, check if this is an issue

    base_page \
        .open_user_menu() \
        .log_out()
