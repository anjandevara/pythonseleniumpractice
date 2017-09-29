import time
from selenium import webdriver

driver = webdriver.Chrome("/Users/anjandevara/Documents/pythonselenium/chromedriver")
driver.get("https://www.yatra.com")

time.sleep(8)
print(driver.title)

driver.quit()