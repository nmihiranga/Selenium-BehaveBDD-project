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


@given(u'I navigated to the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://tech-demo.scandipwa.com/')
    context.driver.find_element(By.ID, 'myAccount').click()
    time.sleep(3)


@when(u'I enter valid email and valid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, 'email').send_keys('test@testt.com')
    context.driver.find_element(By.ID, 'password').send_keys('A111$bbb')
    time.sleep(3)


@when(u'I click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div/section/header/nav/div[2]/div[1]/div/div/div/form/div[3]/button').click()
    time.sleep(3)


@then(u'I should get logged in')
def step_impl(context):
    time.sleep(5)
    expectedText = 'Welcome, testFirst!'
    assert context.driver.find_element(By.XPATH, '//*[@id="root"]/div/section/header/nav/div[2]/div[1]/div[1]').text.__eq__(expectedText)



@when(u'I enter invalid email and valid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, 'email').send_keys('test@invalid.com')
    context.driver.find_element(By.ID, 'password').send_keys('A111$bbb')
    time.sleep(3)


@then(u'I should get a proper warning message')
def step_impl(context):
    try:
        alert = context.driver.switch_to.alert
        alertText = alert.text
        expectedText = 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
        assert alertText.__eq__(expectedText)
        return True
    except UnexpectedAlertPresentException:
        return False
    except NoAlertPresentException:
        return False


@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, 'email').send_keys('test@testt.com')
    context.driver.find_element(By.ID, 'password').send_keys('invalid')
    time.sleep(3)


@when(u'I enter invalid email and invalid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, 'email').send_keys('test@invalid.com')
    context.driver.find_element(By.ID, 'password').send_keys('invalid')
    time.sleep(3)


@when(u'I don\'t enter anything into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, 'email').send_keys('')
    context.driver.find_element(By.ID, 'password').send_keys('')
    time.sleep(3)


@then(u'I should get a warning message to fill required fields')
def step_impl(context):
    expectedText = 'This field is required!'
    assert context.driver.find_element(By.XPATH, '//*[@id="root"]/div/section/header/nav/div[2]/div[1]/div/div/div/form/div[1]/div[2]/div').text.__eq__(expectedText)
