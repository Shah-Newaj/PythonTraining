from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

#is_displayed()   is_enbaled()
searchbox = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Display Status: ",searchbox.is_displayed()) #True
print("Display Status: ",searchbox.is_enabled()) #True

driver.quit()