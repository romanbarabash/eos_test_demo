from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    class __WebDriver:
        def __init__(self):
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.get_options())
            self.driver.implicitly_wait(10)

        def get_options(self):
            options = webdriver.ChromeOptions()
            options.add_argument("disable-infobars")
            options.add_argument("start-maximized")
            options.add_argument("disable-dev-shm-usage")
            options.add_argument("no-sandbox")
            options.add_argument("incognito")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_argument("disable-blink-features=AutomationControlled")
            return options

    driver = None

    def __init__(self):
        if not self.driver:
            Browser.driver = Browser.__WebDriver().driver

driver =