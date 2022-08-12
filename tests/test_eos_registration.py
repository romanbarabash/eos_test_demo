import pytest


@pytest.mark.usefixtures('open_browser',
                         'user_registration',
                         'confirm_registration')
def test_eos_registration(base_page, get_user):
    base_page \
        .verify_user_menu_account(get_user)
