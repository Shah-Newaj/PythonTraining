from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider = driver.find_element(By.XPATH,"//span[1]")
max_slider = driver.find_element(By.XPATH,"//span[2]")

print("Location of Sliders before moving............")
print(min_slider.location)          #{'x': 59, 'y': 250}
print(max_slider.location)          #{'x': 545, 'y': 250}

act = ActionChains(driver)

act.drag_and_drop_by_offset(min_slider, 100, 0).perform()
act.drag_and_drop_by_offset(max_slider, -39, 0).perform()

print("Location of Sliders after moving............")
print(min_slider.location)          #{'x': 59, 'y': 250}
print(max_slider.location)          #{'x': 545, 'y': 250}