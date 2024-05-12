from selenium import webdriver
from utilities import ConfigReader


def before_scenario(context, driver):
    browser = ConfigReader.read_config('basic info', 'browser')

    if browser.__eq__('chrome'):
        context.driver = webdriver.Chrome()
    if browser.__eq__('firefox'):
        context.driver = webdriver.Firefox()
    if browser.__eq__('edge'):
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_config('basic info', 'url'))

def after_scenario(context, driver):
    context.driver.quit()