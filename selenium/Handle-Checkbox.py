#Author: Aishwarya Muralidhar
#This file consists of examples of handling checkboxes in multiple ways using Selenium.
#I am using pratice test automation website "https://itera-qa.azurewebsites.net/home/automation"
# I have put sleep after every functionality just to see the action clearly. This can be removed in production environment

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service  = Service(executable_path="/Users/aishwarya/Downloads/chromedriver_mac64/chromedriver")
driver = webdriver.Chrome(service = service)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

all_days = driver.find_elements(By.XPATH, "//input[@type = 'checkbox' and contains(@id, 'day')]")

# Deselect the selected checkbox
def deselect():
    for day in all_days:
        if day.is_selected():
            day.click()

# Select specific checkbox
driver.find_element(By.XPATH, "//input[@id='wednesday']").click()
time.sleep(5)
deselect()
time.sleep(5)

#Select all checkboxes
for day in all_days:
    day.click()
time.sleep(5)
deselect()
time.sleep(5)

#Select Multiple checkboxes by choice
for day in all_days:
    week_name= day.get_attribute('id')
    if week_name== 'monday' or week_name== 'sunday':
        day.click()
time.sleep(5)
deselect()
time.sleep(5)

#Select last 2 checkboxes
for i in range(len(all_days)-2, len(all_days)):
    all_days[i].click()
time.sleep(5)
deselect()
time.sleep(5)

#Select first 2 checkboxes
for i in range(len(all_days)):
    if i<2:
        all_days[i].click()
time.sleep(5)
deselect()
time.sleep(5)

driver.quit()
