from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
import os




class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email_id = 'email'
    password_id = 'password'
    login_btn_xpath = '//*[@id="root"]/div/section/header/nav/div[2]/div[1]/div/div/div/form/div[3]/button'
    fill_required_fields_warning_xpath = '//*[@id="root"]/div/section/header/nav/div[2]/div[1]/div/div/div/form/div[1]/div[2]/div'
    create_account_xpath = '//*[@id="root"]/div/section/header/nav/div[2]/div[1]/div/div/div/article/section/button'

    login_details_incorrect_warning = 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
    fill_required_fields_warning = 'This field is required!'

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def enter_password(self, pwd):
        self.driver.find_element(By.ID, self.password_id).send_keys(pwd)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def login_details_incorrect_warning_message(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            assert alert_text.__eq__(self.login_details_incorrect_warning)
            return True
        except UnexpectedAlertPresentException:
            return False
        except NoAlertPresentException:
            return False

    def fill_required_fields_warning_message(self):
        assert self.driver.find_element(By.XPATH, self.fill_required_fields_warning_xpath).text.__eq__(self.fill_required_fields_warning)

    def click_create_account(self):
        self.driver.find_element(By.XPATH, self.create_account_xpath).click()