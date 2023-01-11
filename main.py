# Old API /	New API
# find_element_by_id(‘id’) /	find_element(By.ID, ‘id’)
# find_element_by_name(‘name’)	/ find_element(By.NAME, ‘name’)
# find_element_by_xpath(‘xpath’)	/ find_element(By.XPATH, ‘xpath’)
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

os.environ['PATH'] += ':/usr/local/bin'
driver = webdriver.Chrome()

driver.get("https://www.dofactory.com/html/button/id#:~:text=The%20id%20attribute%20assigns%20an%20identifier%20to%20the,to%20any%20HTML%20element.%20A%20unique%20alphanumeric%20string.")
driver.implicitly_wait(30)
myElement = driver.find_element(By.ID, "alert-button")
myElement.click()
myElement = driver.find_element(By.ID, "random")
time.sleep(5)

