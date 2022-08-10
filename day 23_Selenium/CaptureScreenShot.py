from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.save_screenshot("C:\\Users\\Server\\PycharmProjects\\PythonTraining\\day 23_Selenium\\home.png")
driver.save_screenshot(os.getcwd()+"\\homepage.png")

driver.quit()