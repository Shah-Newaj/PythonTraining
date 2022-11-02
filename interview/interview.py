import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

# driver.get("https://demo.zeuz.ai/web/level/one/actions/save_text")
# driver.maximize_window()
#
# text=driver.find_element(By.ID,"randomText").text
# driver.find_element(By.XPATH,"//input[@id='enter_text']").send_keys(text)
#
# text2 = driver.find_element(By.XPATH,"//button[@id='verify_id']").click()
#
# act_text="You have successfully verified the text"
# exp_text= driver.find_element(By.ID,"text_showing").text
#
# if act_text==exp_text:
#     print("success")

# driver.close()
num = 19
flag = False
# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")