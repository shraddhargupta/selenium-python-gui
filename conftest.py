from pytest import fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from src.main.utility import generic_utilities

@fixture(scope='function')
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    yield browser

    browser.quit()


def pytest_addoption(parser):
        parser.addoption(
            "--env",
            action="store",
            help="Environment to run tests against",


            )
        parser.addoption(
            "--config",
            action="store",
            help="Config to run tests against",


        )


@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@fixture(scope='session')
def app_config(request):
    config_filename=request.config.getoption("--config")
    app_config = generic_utilities.read_config_details("/Users/shraddha/Documents/gui-testing-python/guitestingpython/src/main/config/"+config_filename)
    return app_config