from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#open alert window
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
time.sleep(5)

alertwindow = driver.switch_to.alert
print(alertwindow.text)

alertwindow.send_keys("Welcome")
# alertwindow.accept() #close alert window by using OK button
alertwindow.dismiss() #close alert window by using Cancel button