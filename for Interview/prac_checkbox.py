from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demoqa.com/checkbox")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[@title='Toggle']//*[name()='svg']").click()
driver.find_element(By.XPATH,"//label[@for='tree-node-documents']//span[@class='rct-checkbox']//*[name()='svg']").click()
