from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time


driver = webdriver.Chrome()
#driver.implicitly_wait(5)
driver.get("http://suninjuly.github.io/cats.html")



try:
   button = driver.find_element(By.ID, "button")
   
   
finally:
    
    driver.quit()



