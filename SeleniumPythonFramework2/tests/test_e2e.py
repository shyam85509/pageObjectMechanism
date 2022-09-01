import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutPage import CheckOut
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from tests.test_e2edemo import driver
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):

        #self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        homepage = HomePage(self.driver)
        checkOutPage = homepage.shopeItems()
        cardtitls = CheckOut(self.driver)
        cardtitls.cardtitle()
        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
        #self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        checkButton = CheckOut(self.driver)
        checkButton.cheOutButton().click()

        #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        secondCheckButton = CheckOut(self.driver)
        secondCheckButton.checkSecond().click()


        #self.driver.find_element(By.ID, "country").send_keys("ind")
        insertContryName = ConfirmPage(self.driver)
        insertContryName.contryName().send_keys("ind")

        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        #self.driver.find_element(By.LINK_TEXT, "India").click()
        sContry = ConfirmPage(self.driver)
        sContry.selectContryFunction().click()

        #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        checkBoxVariable = ConfirmPage(self.driver)
        checkBoxVariable.checkBoxFunction().click()

        #self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        purchaseButton = ConfirmPage(self.driver)
        purchaseButton.confirmSubFunction().click()

        successtext = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in successtext
        self.driver.get_screenshot_as_file("screen.png")