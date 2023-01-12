import booking_package.constants as const
import os
from selenium import webdriver


class Booking(webdriver.Chrome):
  def __init__(self, driver_path=const.DRIVER_PATH, teardown=False):
    self.driver_path = driver_path 
    self.teardown = teardown
    os.environ['PATH'] += self.driver_path # add the driver to the PATH or else Selenium will complain
    super(Booking, self).__init__() # this is the same as super().__init__()
    self.implicitly_wait(15) # wait for 10 seconds 
    self.maximize_window()
  
  def __exit__(self, exc_type, exc_value, traceback): # default parameters
    if self.teardown:
      self.quit()

  def land_first_page(self):
    self.get(const.BASE_URL)