from selenium import webdriver

driver = webdriver.Chrome('/Users/anjandevara/Documents/pythonselenium/chromedriver')
driver.maximize_window()
driver.get('http://example.com')
html_source = driver.page_source
print(html_source)