import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('C:\\Users\\Dexp\\PycharmProjects\\SeleniumTest\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standart_user = 'standard_use'
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standart_user)
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
button_login = driver.find_element(By.XPATH, "//input[@value='Login']")
button_login.click()
error_msg = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_error_msg = error_msg.text
assert value_error_msg == 'Epic sadface: Username and password do not match any user in this service'
print('Good test')
driver.refresh()
time.sleep(4)