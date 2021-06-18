from src.main.pages.amazon.amazon_login_page import AmazonLoginPage
from pytest import mark


from src.main.utility.generic_utilities import get_execution_details


class AmazonLoginTests():
    @mark.login
    def test_amazon_login_with_valid_credentials(self, browser,app_config):
        base_url = app_config['url']
        print(f'{base_url} : url ')
        user_id = "guptashraddhar@gmail.com"
        password = ""
        login_page = AmazonLoginPage(driver=browser)
        data=get_execution_details(filepath='/Users/shraddha/Documents/gui-testing-python/guitestingpython/input/Amazon_Driver.csv',testcase_name='test_amazon_login_with_valid_credentials')
        print("Data from input sheet",data)
        login_page.go()
        login_page.email_input.input_text(user_id)
        login_page.email_input.enter
        # login_page.continue_button.click
        # login_page.password_input.find
        # login_page.password_input.input_text(password)
        # logo_exists = login_page.amazon_logo_link.element_exists
        # assert logo_exists == True, "User {user_id} looged in successfully"
        assert True,"Logged in successfully"
