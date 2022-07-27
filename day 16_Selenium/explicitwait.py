from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception]) #explicit wait declaration


driver.get("https://www.google.com/")
driver.maximize_window()

searchbox = driver.find_element(By.NAME,'q')
searchbox.send_keys("Selenium")
searchbox.submit()

searchlink = mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[normalize-space()='Selenium']")))
searchlink.click()

driver.quit()

