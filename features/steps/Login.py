from behave import *
import time
from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage


@given(u'I navigated to the login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_my_account()
    time.sleep(3)


@when(u'I enter valid {email} and valid {password} into the fields')
def step_impl(context, email, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email(email)
    context.login_page.enter_password(password)
    time.sleep(3)


@when(u'I click on login button')
def step_impl(context):
    context.login_page.click_login_button()
    time.sleep(3)


@then(u'I should get logged in')
def step_impl(context):
    time.sleep(5)
    context.home_page.check_if_logged_successfully()


@when(u'I enter invalid email as {invalid_email} and valid password as {valid_password} into the fields')
def step_impl(context, invalid_email, valid_password):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email(invalid_email)
    context.login_page.enter_password(valid_password)
    time.sleep(3)


@then(u'I should get a proper warning message')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.login_details_incorrect_warning_message()


@when(u'I enter valid email as {valid_email} and invalid password as {invalid_password} into the fields')
def step_impl(context, valid_email, invalid_password):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email(valid_email)
    context.login_page.enter_password(invalid_password)
    time.sleep(3)


@when(u'I enter invalid email as {invalid_email} and invalid password as {invalid_password} into the fields')
def step_impl(context, invalid_email, invalid_password):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email(invalid_email)
    context.login_page.enter_password(invalid_password)
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
