from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from features.pages.HomePage import HomePage
from features.pages.SearchResultsPage import SearchResultsPage


@given(u'I got navigated to the home page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.check_homepage_title()


@when(u'I enter a valid product into the search box')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_search_product('xbox')
    time.sleep(3)


@when(u'I press enter key')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.press_enter_key()
    time.sleep(10)


@then(u'Valid product should get displayed in search results')
def step_impl(context):
    context.search_results_page = SearchResultsPage(context.driver)
    context.search_results_page.display_valid_product()
    time.sleep(3)


@when(u'I enter a invalid product into the search box')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.enter_search_product('invalid')
    time.sleep(3)


@then(u'product not found message should displayed in search results')
def step_impl(context):
    context.search_results_page = SearchResultsPage(context.driver)
    context.search_results_page.display_product_not_found_message()
    time.sleep(3)