from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    price_elem = WebDriverWait(browser, 12).until(EC.presence_of_element_located((By.XPATH, '//h5[text()="$100"]')))
    
    button = browser.find_element_by_id("book")
    button.click()
       
    first_elem = browser.find_element_by_id("input_value")
    first = int(first_elem.text)
            
    y = calc(first)
    
    text = browser.find_element_by_id("answer")
    text.send_keys(y)
    
    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
