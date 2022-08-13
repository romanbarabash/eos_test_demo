from selenium.common import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CustomSeleniumActions():

    def __init__(self, driver):
        self.driver = driver

    def click_till_element_not_attached(self, element, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        while True:
            try:
                wait.until(EC.element_to_be_clickable((element)))
                element.click()
            except StaleElementReferenceException:
                break
