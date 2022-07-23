from selenium import webdriver
from selenium.webdriver.common.by import By

# serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)

driver = webdriver.Chrome()

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

# classname and tag name

sliders = driver.find_elements(By.CLASS_NAME,"homeslider-container")
print(len(sliders)) # 5 total number of sliders on homepage

links = driver.find_elements(By.TAG_NAME,"a")
print(len(links)) #149 total number of links
