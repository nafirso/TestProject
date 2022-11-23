import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('C:\\Users\\Dexp\\PycharmProjects\\SeleniumTest\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('http://ts1.handifox.online')
driver.maximize_window()
user_name = driver.find_element(By.XPATH, '//input[@id="Email"]')
user_name.send_keys("nik@123.com")
password = driver.find_element(By.XPATH, '//input[@id="Password"]')
password.send_keys("A1234567")
time.sleep(10)

