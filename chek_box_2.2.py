from selenium.webdriver.support.ui import Select
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
assert True



# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/selects1.html')
# x = browser.find_element_by_id('num1').text
# y = browser.find_element_by_id('num2').text
# sum = int(x) + int(y)
# select = browser.find_element_by_id('dropdown')
# select.click()
# sel = Select(select)
# sel.select_by_value(str(sum))
# button = browser.find_element_by_class_name('btn.btn-default')
# button.click()
# time.sleep(3)




