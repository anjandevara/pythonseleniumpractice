from selenium import webdriver

incognito = webdriver.ChromeOptions()
incognito.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=incognito)

driver.get('http://bing.com')