from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')
id_ = browser.find_element_by_id('treasure')
x = id_.get_attribute('valuex')
y = calc(x)
text_box = browser.find_element_by_id('answer')
text_box.send_keys(y)
chek_box = browser.find_element_by_id('robotCheckbox')
chek_box.click()
radio_but = browser.find_element_by_css_selector('[value="robots"]')
radio_but.click()
button = browser.find_element_by_class_name('btn.btn-default')
button.click()


time.sleep(3)
browser.quit()


