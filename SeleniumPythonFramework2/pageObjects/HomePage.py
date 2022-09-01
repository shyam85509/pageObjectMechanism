
#self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOut


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopeItems(self):
        self.driver.find_element(*HomePage.shop).click()
        cardtitls = CheckOut(self.driver)
        return cardtitls