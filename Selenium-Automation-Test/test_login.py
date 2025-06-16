from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_and_navigation(browser):
    browser.get("https://www.myfitnesspal.com/account/login")
    
    time.sleep(2)
    
    email_field = browser.find_element(By.ID, "email")
    email_field.send_keys("xxxxxxxx")
    
    password_field = browser.find_element(By.ID, "password")
    password_field.send_keys("xxxxxxxx")
    
    time.sleep(3)

    login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    
    time.sleep(3)
    
    assert "home" in browser.current_url.lower()