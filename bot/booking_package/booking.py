import booking_package.constants as const
import os
from selenium import webdriver


class Booking(webdriver.Chrome):
  def __init__(self, driver_path=r"/usr/local/bin/chromedriver", implicit_wait=10):
    self.driver_path = driver_path 
    os.environ['PATH'] += self.driver_path # add the driver to the PATH or else Selenium will complain
    super(Booking, self).__init__() # this is the same as super().__init__()

  def land_first_page(self):
    self.get(const.BASE_URL)