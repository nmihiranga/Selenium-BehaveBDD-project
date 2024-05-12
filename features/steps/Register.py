from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
import os




@given(u'I navigate to the register page')
def step_impl(context):
    context.driver.find_element(By.ID, 'myAccount').click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div/section/header/nav/div[2]/div[1]/div/div/div/article/section/button').click()
    time.sleep(3)


@when(u'I enter details into required fields')
def step_impl(context):
    context.driver.find_element(By.ID, 'firstname').send_keys('test')
    context.driver.find_element(By.ID, 'lastname').send_keys('test')
    context.driver.find_element(By.ID, 'email').send_keys('testn@n.com')
    context.driver.find_element(By.ID, 'password').send_keys('A111$bbb')
    context.driver.find_element(By.ID, 'confirm_password').send_keys('A111$bbb')
    time.sleep(3)


@when(u'I click on continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div/section/header/nav/div[2]/div[1]/div/div/div/form/div/button').click()
    time.sleep(3)


@when(u'I enter details into all fields except email')
def step_impl(context):
    context.driver.find_element(By.ID, 'firstname').send_keys('test')
    context.driver.find_element(By.ID, 'lastname').send_keys('test')
    context.driver.find_element(By.ID, 'password').send_keys('A111$bbb')
    context.driver.find_element(By.ID, 'confirm_password').send_keys('A111$bbb')
    time.sleep(3)


@when(u'I enter already registered email into email field')
def step_impl(context):
    context.driver.find_element(By.ID, 'email').send_keys('testn@n.com')
    time.sleep(3)


@then(u'Warning message about existing email should be displayed')
def step_impl(context):
    try:
        alert = context.driver.switch_to.alert
        alertText = alert.text
        expectedText = 'A customer with the same email address already exists in an associated website. '
        assert alertText.__eq__(expectedText)
        return True
    except UnexpectedAlertPresentException:
        return False
    except NoAlertPresentException:
        return False



@then(u'I don\'t enter anything into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, 'firstname').send_keys('')
    context.driver.find_element(By.ID, 'lastname').send_keys('')
    context.driver.find_element(By.ID, 'password').send_keys('')
    context.driver.find_element(By.ID, 'confirm_password').send_keys('')
    time.sleep(3)


@then(u'Warning message about filling required fields should be displayed')
def step_impl(context):
    try:
        alert = context.driver.switch_to.alert
        alertText = alert.text
        expectedText = 'Incorrect data! Please resolve all field validation errors.'
        assert alertText.__eq__(expectedText)
        return True
    except UnexpectedAlertPresentException:
        return False
    except NoAlertPresentException:
        return False
