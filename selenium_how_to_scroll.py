from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('/Users/anjandevara/Documents/pythonselenium/chromedriver')
browser.get('http://wikipedia.org')
elm = browser.find_element_by_tag_name('html')
elm.send_keys(Keys.END)
time.sleep(4)
elm.send_keys(Keys.HOME)

browser.quit()