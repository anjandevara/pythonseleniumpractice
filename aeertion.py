from  selenium import webdriver

driver = webdriver.Chrome('/Users/anjandevara/Documents/pythonselenium/chromedriver')
driver.get('http://google.com')

try:
    assert 'Google' in driver.title
    print('Assertion Passed')

except Exception as e:
    print('Assertion failed', format(e))

driver.quit()