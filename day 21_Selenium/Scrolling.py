from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# Approach 1.Scroll down by Pixel
# driver.execute_script("window.scrollBy(0,3000)","")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of Pixels moved: ",value) #3000

# Approach 2.Scroll till the Element is Visible
# flag = driver.find_element(By.XPATH,"//img[@alt='Flag of Pakistan']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of Pixels moved: ",value)

# Approach 3.Scroll down till end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of Pixels moved: ",value)

time.sleep(3)
# Scroll up to starting point
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of Pixels moved: ",value)