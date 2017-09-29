import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/anjandevara/Documents/pythonselenium/chromedriver')
driver.get('https://www.zkoss.org/zksandbox/#f7')

for i in driver.find_elements_by_xpath('//*[@type="radio"]'):
    i.click()

time.sleep(6)
