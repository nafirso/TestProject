import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('C:\\Users\\Dexp\\PycharmProjects\\SeleniumTest\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
# user_name = driver.find_element(By.ID, "user-name") #ID
# user_name = driver.find_element(By.NAME, "user-name") #Name
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys('standard_user')
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys('secret_sauce')
button_login = driver.find_element(By.XPATH, "//input[@value='Login']" )
button_login.click()
time.sleep(4)