from selenium import webdriver
from selenium.webdriver.common.keys import Keys

while True:
    query = input("Google:")
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    driver.find_element_by_name("q").send_keys(query + Keys.ENTER)