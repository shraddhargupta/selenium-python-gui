from selenium.webdriver.common.by import By
from src.main.base.base_element import BaseElement
from src.main.base.base_page import BasePage
from src.main.base.locator import Locator


class AmazonLoginPage(BasePage):
    url="https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"



    @property
    def email_input(self):
        locator = Locator(by=By.NAME, value="email")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
    @property
    def continue_button(self):
        locator = Locator(by=By.XPATH, value="//input[@id='continue'][@class='a-button-input']")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
    @property
    def password_input(self):
        locator = Locator(by=By.ID, value="ap_password")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
    @property
    def amazon_logo_link(self):
        locator = Locator(by=By.ID, value="nav-logo-sprites")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

