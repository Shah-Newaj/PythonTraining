from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import mysql.connector

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
try:
    con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb")
    curs = con.cursor()  # Create Cursor
    curs.execute("select * from caldata")  # execute query through cursor

    for row in curs:
        # reading data from database
        pric = row[0]
        rateofinterest = row[1]
        per1 = row[2]
        per2 = row[3]
        fre = row[4]
        exp_mvalue = row[5]

        # passing value to the application
        driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(pric)
        driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rateofinterest)
        driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)

        perioddrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
        perioddrp.select_by_visible_text(per2)

        frequencydrp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
        frequencydrp.select_by_visible_text(fre)

        driver.find_element(By.XPATH, "//div[@class='cal_div']//a[1]").click()  # Calculate button

        act_mvalue = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

        # validation
        if float(exp_mvalue) == float(act_mvalue):
            print("Test Passed")

        else:
            print("Test Failed")

        driver.find_element(By.XPATH, "//div[@class='PT25']//a[2]").click()  # Click on Clear button so all the field empty
        time.sleep(2)
    con.close()
except:
    print("Connection Unsuccessful")
driver.close()

