from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    driver = None

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
            options.add_argument("disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            return options

    def __init__(self):
        if not self.driver:
            Browser.driver = Browser.__WebDriver().driver


browser = Browser()
