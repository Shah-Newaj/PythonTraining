import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# xpath
# driver.find_element(By.XPATH,"//input[@id='small-searchterms']").send_keys("Android Mobile")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()

# link text
driver.find_element(By.LINK_TEXT,"Register").click()

time.sleep(5)

driver.close()