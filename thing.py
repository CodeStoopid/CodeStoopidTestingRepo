import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



url = 'https://vanssx3.github.io/Snipema'
un = 'yorker'
pw = 'yorker2'
r = requests.get(url)
print(r.text)

driver = webdriver.Chrome()
driver.get("https://vanssx3.github.io/Snipema")
inputElement = driver.find_element_by_id("aboveBox")
inputElement.send_keys('test')
