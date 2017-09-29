from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome('/Users/anjandevara/Documents/pythonselenium/chromedriver')
driver.get('http://demos.dojotoolkit.org/dijit/tests/form/test_CheckBox.html')

for i in range(20):
    try:
        driver.find_element_by_xpath(".//*[contains(text(),'cb7: normal checkbox.')]").click()
        break
    except NoSuchElementException as e:
        print('retry')
        time.sleep(1)

else:
    print('Test Failed')

driver.quit()