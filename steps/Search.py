from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


@given(u'I got navigated to the home page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://tech-demo.scandipwa.com/')


@when(u'I enter a valid product into the search box')
def step_impl(context):
    context.driver.find_element(By.ID, 'search-field').send_keys('xbox')
    time.sleep(3)


@when(u'I click on search button')
def step_impl(context):
    context.driver.find_element(By.ID, 'search-field').send_keys(Keys.ENTER)
    time.sleep(5)


@then(u'Valid product should get displayed in search results')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/main/section/div/div[2]/div/ul/li[1]/a/div/div[1]/figure/div/img').is_displayed()
    time.sleep(3)


@when(u'I enter a invalid product into the search box')
def step_impl(context):
    context.driver.find_element(By.ID, 'search-field').send_keys('invalid')
    time.sleep(3)


@then(u'product not found message should displayed in search results')
def step_impl(context):
    expectedText = 'There Were No Products Found Matching Your Request.'
    assert context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/main/section/div/div[2]/div/div/h3').text.__eq__(expectedText)
    time.sleep(3)