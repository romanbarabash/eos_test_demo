import pytest


@pytest.mark.usefixtures('user_registration',
                         'confirm_registration',
                         'log_out',
                         'close_browser')
def test_eos_login(base_page, sign_up_page, get_user):
    sign_up_page \
        .open_page() \
        .sign_in(user=get_user)

    base_page \
        .verify_user_menu_account(get_user)
