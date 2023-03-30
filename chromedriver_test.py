from selenium import webdriver

try:
    driver = webdriver.Chrome()
    print("Selenium Chrome webdriver is installed.")
    driver.quit()
except:
    print("Selenium Chrome webdriver is not installed.")
