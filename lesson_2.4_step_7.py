from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import math
import time


driver = webdriver.Chrome()
#driver.implicitly_wait(5)
driver.get("http://suninjuly.github.io/wait2.html")



try:
   button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
        )
   button.click()
   message = driver.find_element(By.ID, "verify_message")
   
   assert "successful" in message.text
   
   
finally:
    
    driver.quit()



