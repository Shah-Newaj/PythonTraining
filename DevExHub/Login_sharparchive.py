import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://dev.sharparchive.com/")
driver.maximize_window()
# -------- Log In --------------
driver.find_element(By.XPATH,"//button[normalize-space()='Accept Cookies']").click()
driver.find_element(By.XPATH,"//span[@class='inline-block whitespace-nowrap']").click()
time.sleep(5)
driver.find_element(By.XPATH,"(//input[@placeholder='Email'])[1]").send_keys("s.n.shuvro@gmail.com")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("!@#123456789ABCdef")
driver.find_element(By.XPATH,"//p[normalize-space()='Login']").click()
# -----------------------------------------------------------------------------------

# ----------------- Edit Address --------------------------------
# time.sleep(10)
# driver.find_element(By.XPATH,"//button[normalize-space()='Cancel']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//p[@class='text-xl font-bold lg:block hidden name-color']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//p[@class='text-gray-1100 xl:text-xl md:text-lg text-xl opacity-50 break-all']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='address']").send_keys("43, House no: 100, CWN (A Rd 35, Dhaka 1212")
time.sleep(5)
driver.find_element(By.XPATH,"//span[normalize-space()='Save']").click()
# ---------------------------------------------------------

# --------------------- Search -----------------------------
time.sleep(5)
driver.find_element(By.XPATH,"//a[@href='/search']//div[@class='link__title']//*[name()='svg']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("Testing")
time.sleep(5)
driver.find_element(By.XPATH,"//span[normalize-space()='Search']").click()
# -----------------------------------------------------------------

# ------------ Log Out -----------
time.sleep(10)
driver.find_element(By.XPATH,"//p[@class='text-xl font-bold lg:block hidden name-color']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//div[@class='rounded-full relative flex items-center justify-around']//span[contains(text(),'Log Out')]").click()
# -----------------------------------------------------------------------------------------
