from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    firstname_id = 'firstname'
    lastname_id = 'lastname'
    email_id = 'email'
    password_id = 'password'
    confirm_password_id = 'confirm_password'
    signup_button_xpath = '//*[@id="root"]/div/section/header/nav/div[2]/div[1]/div/div/div/form/div/button'

    existing_email_warning_message = 'A customer with the same email address already exists in an associated website. '
    field_validation_warning_message = 'Incorrect data! Please resolve all field validation errors.'


    def enter_firstname(self, firstname):
        self.driver.find_element(By.ID, self.firstname_id).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.ID, self.lastname_id).send_keys(lastname)

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.ID, self.confirm_password_id).send_keys(confirm_password)

    def click_signup_button(self):
        self.driver.find_element(By.XPATH, self.signup_button_xpath).click()

    def existing_email_warning(self):
        try:
            alert = self.driver.switch_to.alert
            alertText = alert.text
            assert alertText.__eq__(self.existing_email_warning_message)
            return True
        except UnexpectedAlertPresentException:
            return False
        except NoAlertPresentException:
            return False

    def field_validation_warning(self):
        try:
            alert = self.driver.switch_to.alert
            alertText = alert.text
            assert alertText.__eq__(self.field_validation_warning_message)
            return True
        except UnexpectedAlertPresentException:
            return False
        except NoAlertPresentException:
            return False
