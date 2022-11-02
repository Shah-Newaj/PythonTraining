from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

fullname = driver.find_element(By.ID,"userName")
email = driver.find_element(By.ID,"userEmail")
current_address = driver.find_element(By.ID,"currentAddress")
permanent_address = driver.find_element(By.ID,"permanentAddress")

fullname.send_keys("Shah Newaj")
email.send_keys("newajuiucse@gmail.com")
current_address.send_keys("Dhaka")
permanent_address.send_keys("Rajshahi")
