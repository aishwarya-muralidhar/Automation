from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import sys

n = len(sys.argv)
if n!=3:
    print("Please enter username and password as command line arguments")
    sys.exit(-1)

service = Service("/Users/aishwarya/Downloads/chromedriver_mac64/chromedriver")
driver = webdriver.Chrome(service = service)
driver.get("https://www.facebook.com/")
driver.maximize_window()

username = sys.argv[1]
password = sys.argv[2]
driver.find_element(by = By.NAME, value= "email").send_keys(username)
driver.find_element(by = By.NAME, value = "pass").send_keys(password)
time.sleep(2)
driver.find_element(by = By.NAME, value= "login").click()
time.sleep(15)

actual_title = driver.find_element(By.XPATH, "//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x3x7a5m x6prxxf xvq8zen x1s688f x1qq9wsj']").text
expected_title = "Stories"
if expected_title == actual_title:
    print("Test case passed")
else:
    print("Test case failed")
driver.quit()