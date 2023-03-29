from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_google_search():
    # create a WebDriver instance
    driver = webdriver.Chrome()

    # navigate to the Google homepage
    driver.get("https://www.google.com")

    # find the search box element and enter a query
    search_box = driver.find_element(By.NAME,"q")
    search_box.send_keys("pytest selenium")

    # submit the search and wait for the results page to load
    search_box.submit()
    WebDriverWait(driver, 10).until(EC.title_contains("pytest selenium"))

    # verify that the search results contain the expected text
    assert "pytest-selenium" in driver.page_source

    # close the browser
    driver.quit()
