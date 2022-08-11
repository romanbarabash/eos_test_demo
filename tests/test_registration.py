import pytest


@pytest.mark.usefixtures('open_browser')
def test_registration(get_driver, user_registration, confirm_registration):
    driver = get_driver

    # main map page
    search_location_input = driver.find_element(by="xpath", value="//input[@data-id='location-search-input']")
    assert search_location_input.is_displayed()
