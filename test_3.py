import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('C:\\Users\\Dexp\\PycharmProjects\\SeleniumTest\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standart_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standart_user)
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
password.send_keys(Keys.RETURN)
filter = driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
filter.click()
time.sleep(5)
filter.send_keys(Keys.ARROW_DOWN)
time.sleep(5)
filter.send_keys(Keys.RETURN)
time.sleep(5)