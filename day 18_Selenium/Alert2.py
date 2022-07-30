from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()

#open alert window
driver.find_element(By.XPATH,"//input[@value='Login']").click()
time.sleep(5)

driver.switch_to.alert.accept()

driver.close()