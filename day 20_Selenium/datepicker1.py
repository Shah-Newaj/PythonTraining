from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)

driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("05/30/2022")

year = "2020"
month = "December"
date = "25"

while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if mon==month and yr==year:
        break
    else:
        # driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click() #next arrow
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click() #previous arrow

# Select Date
dates = driver.find_elements(By.XPATH,"//table/tbody/tr/td/a")

for ele in dates:
    if ele.text == date:
        ele.click()
        break