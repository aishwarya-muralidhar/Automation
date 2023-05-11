#Author: Aishwarya Muralidhar
#This file consists of handling radiobuttons and to check if a radiobutton is selected or not using Selenium.
#I am using practice test automation website "https://demo.nopcommerce.com/"
# I have put sleep after every functionality just to see the action clearly. This can be removed in production environment

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="/Users/aishwarya/Downloads/chromedriver_mac64/chromedriver")
driver = webdriver.Chrome(service = service)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
time.sleep(3)

#capture radiobuttons
radio_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
radio_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")

#Check the default status of radiobuttons using is_selected() and print the value in console
print("Status of radiobuttons by default:")
print(radio_male.is_selected())
print(radio_female.is_selected())

#Select male radiobutton and check the status of radiobuttons using is_selected() and print the value in console
radio_male.click()
time.sleep(3)
print("Status of radiobuttons after selecting male radiobutton:")
print(radio_male.is_selected())
print(radio_female.is_selected())

#Select female radiobutton and check the status of radiobuttons using is_selected() and print the value in console
radio_female.click()
time.sleep(3)
print("Status of radiobuttons after selecting female radiobutton:")
print(radio_male.is_selected())
print(radio_female.is_selected())

driver.quit()
