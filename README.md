# Selenium_Begin
Selenium is a portable framework for testing web applications. Selenium provides a playback tool for authoring functional tests without the need to learn a test scripting language (Selenium IDE). It also provides a test domain-specific language (Selenese) to write tests in a number of popular programming languages, including C#, Groovy, Java, Perl, PHP, Python, Ruby and Scala. The tests can then run against most modern web browsers. Selenium runs on Windows, Linux, and Mac OS X.

Create user interfaces to test front end websites and automate the process.

* Before Prerequisites
- Python installed
- Pip install selenium

Import the following libraries (main)
- from selenium import webdriver
```python
from selenium import webdriver
```
- Create a driver object
```python
driver = webdriver.Chrome()
```

* Only that will run an exception error - PATH
To fix this error, you need to download the driver for the browser you are using and add it to the PATH variable.


- Driver to download https://chromedriver.chromium.org/downloads

- to check version of chrome, go to chrome://version

as each computer has a different version of chrome and path you need to import in code the path of the driver you downloaded.
```python	
import os
os.environ["PATH"] += r"/Users/username/SeleniumDrivers/chromedriver_win32/chromedriver.exe"
```


The minimum setup it will look like this:
```python
import os
from selenium import webdriver
os.environ["PATH"] += r"/Users/username/SeleniumDrivers/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome()
```

Good Site for Testing is https://www.seleniumeasy.com/test/

1st - Select element to identify
2nd - Select action to perform
3rd - Select value to perform action on

```python	
driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html") # get the url

driver.implicitly_wait(30) # wait for 10 seconds to make sure the page loads - this not wait 30 seconds - time.sleep(30) // wait for 30 seconds

driver.find_element_by_id("downloadButton").click() # find the element by id and click
```

# close the download pop up saying completed
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
progress_element = driver.find_element_by_class_name("progress-label") # find the element by class name

print(f"{progress_element.text == 'Completed!'}") # print the text of the element (false)

# wait for the text to be present in the element
WebDriverWait(driver, 30).until(
  EC.text_to_be_present_in_element(
     (By.CLASS_NAME, "progress-label"), # filter
     "Completed!")) # text to be present in the element

print(f"{progress_element.text == 'Completed!'}") # print the text of the element (true)
```

# Filling Forms Automation

```python
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html") # get the url


```

```python









