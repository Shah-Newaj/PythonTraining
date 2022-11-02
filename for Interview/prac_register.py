from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
#Full name
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Shah")
driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("Newaj")

#Address and Email
driver.find_element(By.XPATH,"//textarea[@class='form-control ng-pristine ng-untouched ng-valid']").send_keys("Rajshahi")
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("newajuiucse@gmail.com")

#Phone
driver.find_element(By.XPATH,"//input[@type='tel']").send_keys("01741387535")

#Gender
driver.find_element(By.XPATH,"//input[@value='Male']").click()

# Hobbies
driver.find_element(By.XPATH,"//input[@id='checkbox3']").click()

#Language Selection
driver.find_element(By.ID,"msdd").click()
driver.find_element(By.XPATH,"//a[normalize-space()='English']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Arabic']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Urdu']").click()