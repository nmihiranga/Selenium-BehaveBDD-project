from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
import os

from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage
from features.pages.RegisterPage import RegisterPage


@given(u'I navigate to the register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_my_account()
    time.sleep(3)
    context.login_page = LoginPage(context.driver)
    context.login_page.click_create_account()
    time.sleep(3)


@when(u'I enter details into required fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_firstname('test')
    context.register_page.enter_lastname('test')
    context.register_page.enter_email('testn@n.com')
    context.register_page.enter_password('A111$bbb')
    context.register_page.enter_confirm_password('A111$bbb')
    time.sleep(3)


@when(u'I click on signup button')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.click_signup_button()
    time.sleep(3)


@when(u'I enter details into all fields except email')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_firstname('test')
    context.register_page.enter_lastname('test')
    context.register_page.enter_password('A111$bbb')
    context.register_page.enter_confirm_password('A111$bbb')
    time.sleep(3)


@when(u'I enter already registered email into email field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_email('testn@n.com')
    time.sleep(3)


@then(u'Warning message about existing email should be displayed')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.existing_email_warning()



@then(u'I don\'t enter anything into the fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_firstname('')
    context.register_page.enter_lastname('')
    context.register_page.enter_email('')
    context.register_page.enter_password('')
    context.register_page.enter_confirm_password('')
    time.sleep(3)


@then(u'Warning message about filling required fields should be displayed')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.field_validation_warning()
