from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#click on Link
# driver.find_element(By.LINK_TEXT,"Digital downloads").click()

#find number of links in a page
links = driver.find_elements(By.XPATH,"//a")
# links = driver.find_elements(By.TAG_NAME,"a")
print("Total nubmer of links: ",len(links))

#print all link names
for link in links:
    print("Link Names: ",link.text)


driver.quit()