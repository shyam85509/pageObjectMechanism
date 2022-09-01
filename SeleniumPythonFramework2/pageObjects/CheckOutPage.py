from selenium.webdriver.common.by import By


class CheckOut:
    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    card = (By.XPATH, "//div[@class='card h-100']")

    # self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click() ==== checkoutButton
    check = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    check2 = (By.XPATH, "//button[@class='btn btn-success']")

    def cardtitle(self):
        return self.driver.find_elements(*CheckOut.card)

    def cheOutButton(self):
        return self.driver.find_element(*CheckOut.check)

    def checkSecond(self):
        return self.driver.find_element(*CheckOut.check2)


