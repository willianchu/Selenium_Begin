# Old API /	New API
# find_element_by_id(‘id’) /	find_element(By.ID, ‘id’)
# find_element_by_name(‘name’)	/ find_element(By.NAME, ‘name’)
# find_element_by_xpath(‘xpath’)	/ find_element(By.XPATH, ‘xpath’)

# Syntax WebElement elm = driver. findElement (By.className ("input__input")); WebElement p = driver.findElement (By.xpath ("//input [@class = ' input__input']")); WebElement t = driver. findElement (By.cssSelector ("input [class=' input__input']"));

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

os.environ['PATH'] += ':/usr/local/bin'
driver = webdriver.Chrome()

driver.get("https://www.lighthouselabs.ca/")
driver.implicitly_wait(30)
myElement = driver.find_element(By.XPATH, "//a[@title='Courses']")
myElement.click()

time.sleep(5)

