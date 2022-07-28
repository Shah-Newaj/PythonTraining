from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# 1.select specific checkbox
# driver.find_element(By.XPATH,"//input[@id='monday']").click()

# 2.select all the checkboxes
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
# print(len(checkboxes)) # 7

# approach 1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()


# approach 2
for check in checkboxes:
    check.click()

# 3.select multiple checkbox by choice
# for check in checkboxes:
#     weekname = check.get_attribute('id')
#     if weekname=='monday' or weekname=='sunday' or weekname=='wednesday':
#         check.click()

# 4. select last 2 checkboxes
# range(5,7)--> 6,7
#totalnumberofelements - 2 = starting index
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()

#5.select 1st 2 checkboxes
# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()

time.sleep(5)
#6. Clearing all the checkboxes
for check in checkboxes:
    if check.is_selected():
        check.click()