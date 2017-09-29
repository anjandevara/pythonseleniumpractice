from selenium import webdriver

driver = webdriver.Chrome('/Users/anjandevara/Documents/pythonselenium/chromedriver')
driver.get('https://onecore.net/')

ids = driver.find_elements_by_xpath('//*[@id]')

for eid in ids:
    print(eid.get_attribute('id'))

driver.quit()