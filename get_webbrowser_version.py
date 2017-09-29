from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome('/Users/anjandevara/Documents/pythonselenium/chromedriver')
browser.get('http://google.com')

asd = browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

print(browser.capabilities['version'])
print(browser.current_url)