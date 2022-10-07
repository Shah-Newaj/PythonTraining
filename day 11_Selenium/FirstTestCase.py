from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)

driver = webdriver.Chrome()

driver.get("http://dceims.bdeducation.org.bd/schoolAdmin")
driver.maximize_window()

driver.find_element(By.NAME,"email").send_keys("marma.newaj@gmail.com")
driver.find_element(By.ID,"password").send_keys("12345678")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

act_title = driver.title
exp_title = "EIMS Dashboard"

if act_title == exp_title:
    print("Login test passed")
else:
    print("Login test failed")

driver.close()



