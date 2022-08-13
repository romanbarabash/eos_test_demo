import pytest


@pytest.mark.usefixtures('close_browser')
def test_eos_registration(base_page, get_user, user_registration, confirm_registration):
    base_page \
        .verify_user_menu_account(get_user)
