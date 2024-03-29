from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import XLUtils # from directory import filename (showed in video) but here working without directory
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

file = "C:\Selenium Practice\caldata.xlsx"  #Excel File Location

rows = XLUtils.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    #reading data from excel
    pric = XLUtils.readData(file,"Sheet1",r,1)
    rateofinterest = XLUtils.readData(file,"Sheet1",r,2)
    per1 = XLUtils.readData(file,"Sheet1",r,3)
    per2 = XLUtils.readData(file,"Sheet1",r,4)
    fre = XLUtils.readData(file,"Sheet1",r,5)
    exp_mvalue = XLUtils.readData(file, "Sheet1", r, 6)

    #passing value to the application
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(pric)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rateofinterest)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)

    perioddrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(per2)

    frequencydrp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    frequencydrp.select_by_visible_text(fre)

    driver.find_element(By.XPATH,"//div[@class='cal_div']//a[1]").click() #Calculate button

    act_mvalue = driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text

    #validation
    if float(exp_mvalue)==float(act_mvalue):
        print("Test Passed")
        XLUtils.writeData(file,"Sheet1",r,8,"Passed")
        XLUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("Test Failed")
        XLUtils.writeData(file, "Sheet1", r, 8, "Failed")
        XLUtils.fillRedColor(file, "Sheet1", r, 8)
    driver.find_element(By.XPATH,"//div[@class='PT25']//a[2]").click() #Click on Clear button so all the field empty
    time.sleep(2)

driver.close()