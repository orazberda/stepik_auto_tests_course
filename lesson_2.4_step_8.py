from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin
import time

def calc(x):
    return str(log(abs(12*sin(int(x)))))


try:
   driver = webdriver.Chrome()
   #driver.implicitly_wait(5)
   driver.get("http://suninjuly.github.io/explicit_wait2.html")
   button = WebDriverWait(driver, 12).until(
          EC.text_to_be_present_in_element((By.ID, "price"),"$100")
       )
   button = driver.find_element(By.ID, 'book')
   button.click()
   x_value = driver.find_element(By.ID, "input_value").text
   result = calc(x_value)

   answer_input = driver.find_element(By.ID, "answer")
   answer_input.send_keys(result)

   submit_button = driver.find_element(By.ID, "solve")
   submit_button.click()
   #message = driver.find_element(By.ID, "verify_message")
   
   #assert "successful" in message.text
   
   
finally:
    time.sleep(5)
    driver.quit()



