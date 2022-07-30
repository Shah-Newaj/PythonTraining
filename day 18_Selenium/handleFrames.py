from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()
#1st select frame then element
driver.switch_to.frame("packageListFrame") #no need to use locator
driver.find_element(By.XPATH,"//a[normalize-space()='org.openqa.selenium']").click()
driver.switch_to.default_content() #going back to main page

driver.switch_to.frame("packageFrame") #no need to use locator
driver.find_element(By.XPATH,"//a[normalize-space()='org.openqa.selenium']").click()
driver.switch_to.default_content() #going back to main page

driver.switch_to.frame("classFrame") #no need to use locator
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]/a").click()
