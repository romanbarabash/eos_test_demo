from selenium.common import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CustomSeleniumActions():

    def __init__(self, driver):
        self.driver = driver

    def click_element_using_actions(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()

    def click_element_using_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def click_element_loop(self, element, timeout=10, poll=0.5):
        wait = WebDriverWait(self.driver, timeout, poll_frequency=poll)
        while True:
            try:
                wait.until(EC.element_to_be_clickable((element)))
                element.click()
            except StaleElementReferenceException:
                break

    def wait_till_element_located_appears(self, locator, timeout=10, poll=0.5):
        wait = WebDriverWait(self.driver, timeout=timeout,
                             ignored_exceptions=(StaleElementReferenceException,
                                                 NoSuchElementException,
                                                 TimeoutException),
                             poll_frequency=poll)
        try:
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return None

    def wait_till_element_located_disappears(self, locator, timeout=10, poll=0.5):
        wait = WebDriverWait(self.driver, timeout=timeout,
                             ignored_exceptions=(StaleElementReferenceException,
                                                 NoSuchElementException,
                                                 TimeoutException),
                             poll_frequency=poll)
        try:
            return wait.until_not(EC.presence_of_element_located(locator))
        except (TimeoutException or NoSuchElementException):
            return None
