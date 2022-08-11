import pytest


@pytest.mark.usefixtures('open_browser')
def test_login(get_user, get_driver, user_registration, log_out):
    user = get_user
    driver = get_driver

    sign_in_form_button = driver.find_element(by="xpath", value="//button[@data-id='sign-in-button']")
    sign_in_form_button.click()

    # registration/sign in form
    email_name_field = driver.find_element(by="xpath", value="//input[@formcontrolname='email']")
    password_name_field = driver.find_element(by="xpath", value="//input[@formcontrolname='password']")
    sign_in_button = driver.find_element(by="xpath", value="//button[@data-id='sign-in-btn']")

    email_name_field.send_keys(user.email)
    password_name_field.send_keys(user.password)
    sign_in_button.click()

    # main map page
    search_location_input = driver.find_element(by="xpath", value="//input[@data-id='location-search-input']")
    assert search_location_input.is_displayed()
