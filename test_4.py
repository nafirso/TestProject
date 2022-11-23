import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
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
time.sleep(4)
# now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
# name_scr = 'screen' + now_date + '.png'
# driver.save_screenshot('C:\\Users\\Dexp\\PycharmProjects\\SeleniumTest\\scr\\' + name_scr)
# time.sleep(4)
# driver.execute_script("window.scrollTo(0, 200)")

action = ActionChains(driver)
red_t_shirt = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
action.move_to_element(red_t_shirt).perform()
time.sleep(5)