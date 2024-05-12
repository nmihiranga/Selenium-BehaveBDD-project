from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
import os

from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage


@given(u'I navigated to the login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_my_account()
    time.sleep(3)


@when(u'I enter valid email and valid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email('test@testt.com')
    context.login_page.enter_password('A111$bbb')
    time.sleep(3)


@when(u'I click on login button')
def step_impl(context):
    context.login_page.click_login_button()
    time.sleep(3)


@then(u'I should get logged in')
def step_impl(context):
    time.sleep(5)
    context.home_page.check_if_logged_successfully()



@when(u'I enter invalid email and valid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email('test@invalid.com')
    context.login_page.enter_password('A111$bbb')
    time.sleep(3)


@then(u'I should get a proper warning message')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.login_details_incorrect_warning_message()


@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email('test@testt.com')
    context.login_page.enter_password('invalid')
    time.sleep(3)


@when(u'I enter invalid email and invalid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email('test@invalid.com')
    context.login_page.enter_password('invalid')
    time.sleep(3)


@when(u'I don\'t enter anything into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email('')
    context.login_page.enter_password('')
    time.sleep(3)


@then(u'I should get a warning message to fill required fields')
def step_impl(context):
    context.login_page.fill_required_fields_warning_message()
