from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)

driver = webdriver.Chrome()

driver.get("http://automationpractice.com")
driver.maximize_window()

# Absolute XPath
# driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[2]/form[1]/input[4]").send_keys("T-shirts")
# driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[2]/form[1]/button[1]").click()

# Relative XPath
driver.find_element(By.XPATH,"//input[@id='search_query_top']").send_keys("T-shirts")
driver.find_element(By.XPATH,"//button[@name='submit_search']").click()