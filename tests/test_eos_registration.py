import pytest


@pytest.mark.usefixtures('user_registration',
                         'confirm_registration',
                         'close_browser')
def test_eos_registration(base_page, get_user):
    base_page \
        .verify_user_menu_account(get_user)
