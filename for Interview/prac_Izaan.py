import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://www.izaanschool.com/")
driver.maximize_window()

#Courses-->courses
courses = driver.find_element(By.XPATH,"//a[@id='navbarCourses']")
qaae = driver.find_element(By.XPATH,"//a[@class='dropdown-link'][normalize-space()='QAAE']")

#Mouse Hover
act = ActionChains(driver)
act.move_to_element(courses).move_to_element(qaae).click().perform()

