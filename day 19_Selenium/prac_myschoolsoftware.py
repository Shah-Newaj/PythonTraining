from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://dceims.bdeducation.org.bd/schoolAdmin")
driver.maximize_window()

#Login
driver.find_element(By.NAME,"email").send_keys("marma.newaj@gmail.com")
driver.find_element(By.ID,"password").send_keys("12345678")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3)

#Student Management->Manage Students-> Inactive Students
driver.find_element(By.XPATH,"//span[normalize-space()='Student Management']").click()
driver.find_element(By.XPATH,"//*[@id='navbarNavDropdown']/ul/li[2]/ul/li[2]/a").click()
driver.find_element(By.XPATH,"//div[contains(text(),'Inactive Students')]").click()


#total rows in a table
rows = len(driver.find_elements(By.XPATH,"//tbody/tr"))
print("total number of rows in a table: ",rows)

count=0
for r in range(2,rows+1):
    status = driver.find_element(By.XPATH,"//tbody/tr["+str(r)+"]/td[6]").text
    if status=="Rose":
        count=count+1

print("Total number of Stduents: ",rows)
print("number of Rose Students: ",count)
print("number of Lily Students: ",(rows-count))

driver.close()