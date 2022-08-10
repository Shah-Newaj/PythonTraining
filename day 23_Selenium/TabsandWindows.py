from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# regilink = Keys.CONTROL+Keys.ENTER #to open in new tab
# driver.find_element(By.LINK_TEXT,"Register").send_keys(regilink)

# Selenium 4 new command - opens a new tab and switches to new tab
# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://www.orangehrm.com/")

# Selenium 4 new command - opens a new browser window and switches to new window
driver.get("https://www.opencart.com/")
driver.switch_to.new_window('window')
driver.get("https://www.orangehrm.com/")