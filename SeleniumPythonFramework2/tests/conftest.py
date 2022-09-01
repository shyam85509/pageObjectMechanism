import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



def pytest_addoption(parser):
    parser.addoption(
        "--browsername", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browsername = request.config.getoption("--browsername")
    if browsername == "chrome":
        s = Service("C:\\chromedriver.exe")
    elif browsername == "firefox":
        s = Service("C:\\geckodriver.exe")
    elif browsername == "IE":
        print("browser open with IE")
    driver = webdriver.Chrome(service=s)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver