from behave import *

@given(u'I got navigated to the home page')
def step_impl(context):
    print('STEP: Given I got navigated to the home page')


@when(u'I enter a valid product into the search box')
def step_impl(context):
    print('STEP: Given I got navigated to the home page')


@when(u'I click on search button')
def step_impl(context):
    print('STEP: Given I got navigated to the home page')


@then(u'Valid product should get displayed in search results')
def step_impl(context):
    print('STEP: Given I got navigated to the home page')


@when(u'I enter a invalid product into the search box')
def step_impl(context):
    print('STEP: Given I got navigated to the home page')


@then(u'product not found message should displayed in search results')
def step_impl(context):
    print('STEP: Given I got navigated to the home page')


@when(u'I don\'t enter anything into the search box')
def step_impl(context):
    print('STEP: Given I got navigated to the home page')
