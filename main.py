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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


os.environ['PATH'] += ':/usr/local/bin'
driver = webdriver.Chrome()

driver.get("https://www.seleniumeasy.com/python/locating-elements-in-selenium-python")
nameID = driver.find_element(By.ID, "edit-name")
nameID.send_keys("Joel Campbell")
commentID = driver.find_element(By.ID, "edit-comment-body-und-0-value")
commentID.send_keys("This is a comment super cool made by Joel Campbell Bot")
time.sleep(5)




# driver.get("lighthouselabs.ca")
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@title='Courses']")))
# # EC.text_to_be_present_in_element((By.XPATH, "//a[@title='Courses']"), "Courses")
# myElement = driver.find_element(By.XPATH, "//a[@title='Courses']")
# myElement.click()
# time.sleep(5)

