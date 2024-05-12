from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    my_account_id = 'myAccount'
    after_login_real_text_xpath = '//*[@id="root"]/div/section/header/nav/div[2]/div[1]/div[1]'
    search_box_id = 'search-field'


    homepage_title = 'Technology Homepage'
    after_login_expected_text = 'Welcome, testFirst!'

    def click_my_account(self):
        self.driver.find_element(By.ID, self.my_account_id).click()

    def check_if_logged_successfully(self):
        assert self.driver.find_element(By.XPATH, self.after_login_real_text_xpath).text.__eq__(self.after_login_expected_text)

    def check_homepage_title(self):
        assert self.driver.title.__eq__(self.homepage_title)

    def enter_search_product(self, product):
        self.driver.find_element(By.ID, self.search_box_id).send_keys(product)

    def press_enter_key(self):
        self.driver.find_element(By.ID, self.search_box_id).send_keys(Keys.ENTER)