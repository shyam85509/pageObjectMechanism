from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.ID, "country").send_keys("ind")
    contry = (By.ID, "country")
    # self.driver.find_element(By.LINK_TEXT, "India").click()
    selectContry = (By.LINK_TEXT, "India")
    #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    #self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    confirmsub = (By.CSS_SELECTOR, "[type='submit']")

    def contryName(self):
        return self.driver.find_element(*ConfirmPage.contry)

    def selectContryFunction(self):
        return self.driver.find_element(*ConfirmPage.selectContry)

    def checkBoxFunction(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def confirmSubFunction(self):
        return self.driver.find_element(*ConfirmPage.confirmsub)