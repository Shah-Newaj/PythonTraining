#we have to install requests package first through python interpreter
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

allLinks = driver.find_elements(By.TAG_NAME,"a")
count=0

for link in allLinks:
    url = link.get_attribute('href')
    try:
        res = requests.head(url) # getting response from server directly through request package
    except:
        None

    if res.status_code>=400:    #checking only the status code
        print(url,"  is broken link")
        count+=1
    else:
        print(url, "  is valid link")

print("Total number of broken links", count)
