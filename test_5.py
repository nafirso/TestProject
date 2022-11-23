import datetime
import time
from selenium import webdriver
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
button_login = driver.find_element(By.XPATH, "//input[@value='Login']")
button_login.click()

hide_menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
hide_menu.click()
time.sleep(4)
link_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
link_about.click()
time.sleep(4)
