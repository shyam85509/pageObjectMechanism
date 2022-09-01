from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "name").send_keys("Shyamsundar")
driver.find_element(By.NAME, "email").send_keys("shyam85509@gmail.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("S#1234567")
driver.find_element(By.XPATH, "//label[@for='exampleCheck1']").click()
#driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']").click()
#We have to select element from select so first collect element and then select it from visible text
select = Select(driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))
select.select_by_visible_text("Female")
driver.find_element(By.XPATH, "//input[@value='option2']").click()
driver.find_element(By.XPATH, "//input[@type='date']").send_keys("16-11-1991")
driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()