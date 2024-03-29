from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

#Login
driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()
time.sleep(3)

#Admin->user management-> users
driver.find_element(By.XPATH,"//*[@id='menu_admin_viewAdminModule']/b").click()
driver.find_element(By.XPATH,"//*[@id='menu_admin_UserManagement']").click()
driver.find_element(By.XPATH,"//*[@id='menu_admin_viewSystemUsers']").click()

#total rows in a table
rows = len(driver.find_elements(By.XPATH,"//table[@id='resultTable']/tbody/tr"))
print("total number of rows in a table: ",rows)

count=0
for r in range(2,rows+1):
    status = driver.find_element(By.XPATH,"//table[@id='resultTable']/tbody/tr["+str(r)+"]/td[5]").text
    if status=="Enabled":
        count=count+1

print("Total number of users: ",rows)
print("number of Enables users: ",count)
print("number of Disabled users: ",(rows-count))

driver.close()

