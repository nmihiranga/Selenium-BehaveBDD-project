from selenium.webdriver.common.by import By


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver

    valid_product_xpath = '//*[@id="root"]/div/div[3]/main/section/div/div[2]/div/ul/li[1]/a/div/div[1]/figure/div/img'
    product_not_found_message_xpath = '//*[@id="root"]/div/div[3]/main/section/div/div[2]/div/div/h3'

    product_not_found_message = 'There Were No Products Found Matching Your Request.'

    def display_valid_product(self):
        assert self.driver.find_element(By.XPATH, self.valid_product_xpath).is_displayed()

    def display_product_not_found_message(self):
        assert self.driver.find_element(By.XPATH, self.product_not_found_message_xpath).text.__eq__(self.product_not_found_message)
