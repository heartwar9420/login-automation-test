from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

URL = "https://the-internet.herokuapp.com/login"

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_login_success(browser):
    browser.get(URL)
    browser.find_element(By.ID, "username").send_keys("tomsmith")
    browser.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)
    message = browser.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in message

def test_login_fail(browser):
    browser.get(URL)
    browser.find_element(By.ID, "username").send_keys("wronguser")
    browser.find_element(By.ID, "password").send_keys("wrongpass")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)
    message = browser.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in message
