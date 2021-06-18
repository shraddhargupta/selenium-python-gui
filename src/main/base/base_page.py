class BasePage(object):

    url=None

    def __init__(self, driver):
        self.driver = driver


    def go(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)