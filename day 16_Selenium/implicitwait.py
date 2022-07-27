from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)

driver = webdriver.Chrome()
driver.implicitly_wait(10) #Seconds


driver.get("https://www.google.com/")
driver.maximize_window()

searchbox = driver.find_element(By.NAME,'q')
searchbox.send_keys("Selenium")
searchbox.submit()

driver.find_element(By.XPATH,"//h3[normalize-space()='Selenium']").click()

driver.quit()

