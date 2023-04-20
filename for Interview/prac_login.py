from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://dceims.bdeducation.org.bd/schoolAdmin")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@placeholder='Email/User ID']").send_keys("marma.newaj@gmail.com")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("12345678")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

act_title = driver.title
exp_title = "EIMS Dashboard"

if act_title==exp_title:
    print("Login test Passed")
else:
    print("Login test Failed")

driver.close()