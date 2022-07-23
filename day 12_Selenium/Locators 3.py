from selenium import webdriver
from selenium.webdriver.common.by import By

# serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)

driver = webdriver.Chrome()

driver.get("https://facebook.com/")
driver.maximize_window()

# CSS Selector
#tag and id
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("marma.newaj")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("marma.newaj")

#tag and class
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("marma.newaj")
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("marma.newaj")

#tag and attribute
# driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("marma.newaj")
# driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("marma.newaj")

#tag, class and attribute
# driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys("marma.newaj")
driver.find_element(By.CSS_SELECTOR,".inputtext[id=pass]").send_keys("newaj")