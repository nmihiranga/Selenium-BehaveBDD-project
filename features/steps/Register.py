from behave import *
import time
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


@when(u'I enter details into required fields as {firstname} {lastname} {email} {password} {confirm_password}')
def step_impl(context, firstname, lastname, email, password, confirm_password):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_firstname(firstname)
    context.register_page.enter_lastname(lastname)
    context.register_page.enter_email(email)
    context.register_page.enter_password(password)
    context.register_page.enter_confirm_password(confirm_password)
    time.sleep(3)


@when(u'I click on signup button')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.click_signup_button()
    time.sleep(5)


@when(u'I enter below details into all fields except email')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    for row in context.table:
        context.register_page.enter_firstname(row['firstname'])
        context.register_page.enter_lastname(row['lastname'])
        context.register_page.enter_password(row['password'])
        context.register_page.enter_confirm_password(row['confirm_password'])
        time.sleep(3)


@when(u'I enter already registered email as {email} into email field')
def step_impl(context, email):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_email(email)
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
