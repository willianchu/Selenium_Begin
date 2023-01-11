# source .venv/bin/activate 
import os
from selenium import webdriver

os.environ['PATH'] += ':/usr/local/bin'
driver = webdriver.Chrome()

driver.get("https://www.lighthouselabs.ca/en")
myElement = driver.find_element_by_class("btn apply-btn")
myElement.click()

# wait 10 seconds for the page to load

driver.implicitly_wait(10)
