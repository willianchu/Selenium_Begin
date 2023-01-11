
import os
from selenium import webdriver


os.environ['PATH'] += ':/usr/local/bin'
driver = webdriver.Chrome()

driver.get("https://www.dofactory.com/html/button/id#:~:text=The%20id%20attribute%20assigns%20an%20identifier%20to%20the,to%20any%20HTML%20element.%20A%20unique%20alphanumeric%20string.")
driver.implicitly_wait(30)
myElement = driver.find_element_by_id("alert-button")
myElement.click()

# wait 10 seconds for the page to load

