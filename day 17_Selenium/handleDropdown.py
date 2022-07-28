from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

drpcountry_element = driver.find_element(By.XPATH,"//select[@id='input-country']")
drpcountry = Select(drpcountry_element)

#select option from the dropdown
# drpcountry.select_by_visible_text("Bangladesh")
# drpcountry.select_by_value("10") #Argentina
# drpcountry.select_by_index(13) #Index

# capture all the options and print them
alloptions = drpcountry.options
print("Total Number of options: ",len(alloptions))

# for opt in alloptions:
#     print(opt.text)

# Select option from dropdown without using buil-in method
for opt in alloptions:
    if opt.text=="Bangladesh":
        opt.click()
        break


# alloptions = driver.find_elements(By.XPATH,"//*[@id='input-country']/option")   #if we want to do same thing without select tag
# print(len(alloptions))