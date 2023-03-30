import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(scope="module")
def driver():
    # Set up Selenium WebDriver
    driver = webdriver.Firefox()
    yield driver
    # Teardown Selenium WebDriver
    driver.quit()

def test_login_logout(driver):
    # Visiting page
    driver.get('https://automationexercise.com/')
    # driver.get('https://automationexercise.com/login')
    # assert "automationexercise" in driver.title
    # Clicking on the login link
    driver.find_element(By.XPATH,'//a[@href="/login"]').click()
    # Filling in email and password fields
    driver.find_element(By.CSS_SELECTOR,'input[data-qa="login-email"]').send_keys('stevenzhang416@gmail.com')
    driver.find_element(By.NAME,'password').send_keys('stevenzhang')
    # Clicking on the login button
    driver.find_element(By.CSS_SELECTOR,'button[type=submit]').click()
    # Verifying that the user is logged in
    # logging.debug('Page source: %s', driver.page_source)
    # print(driver.page_source)
    assert "Logged in as" in driver.page_source
    assert "stevenzhang" in driver.page_source
    # Clicking on the logout link
    driver.find_element(By.XPATH,'//a[@href="/logout"]').click()
    # Verifying that the user is logged out
    assert "Login to your account" in driver.page_source
