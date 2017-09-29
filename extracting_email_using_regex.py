from selenium import webdriver
import re
import time
driver = webdriver.Chrome("/Users/anjandevara/Documents/pythonselenium/chromedriver")
driver.get('http://www.airindia.in/contact-details.htm')

doc = driver.page_source

emails = re.findall(r'[\w\,-]+@[\w\,-]+', doc)

time.sleep(5)
for email in emails:
    print(email)

driver.quit()
