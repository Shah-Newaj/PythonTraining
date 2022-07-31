from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# windowID = driver.current_window_handle
# print(windowID) #dynamic everytime id will be different

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowIds = driver.window_handles

#Approach 1
# parentwindow = windowIds[0]
# childwindow = windowIds[1]
#
# # print(parentwindow,childwindow)
#
# driver.switch_to.window(childwindow)
# print("Title of the Child Window: ",driver.title)
#
# driver.switch_to.window(parentwindow)
# print("Title of the Parent Window: ",driver.title)

#Approach 2
# for winid in windowIds:
#     driver.switch_to.window(winid)
#     print(driver.title)

time.sleep(3)
#close specific browser windows
for winid in windowIds:
    driver.switch_to.window(winid)
    if driver.title=="OrangeHRM" or driver.title=="XYZ" :
        driver.close()