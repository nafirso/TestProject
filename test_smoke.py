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
action = ActionChains(driver)

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standart_user)
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
button_login = driver.find_element(By.XPATH, "//input[@value='Login']")
button_login.click()
product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
price_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price'][1]")
value_price_product_1 = price_product_1.text
add_to_card_bt = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
add_to_card_bt.click()
card_bt = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
card_bt.click()
checkout_bt = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout_bt.click()
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys('Nikolay')
last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys('Firsov')
zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip_code.send_keys('123456')
continue_bt = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_bt.click()
product_1_valid = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1_valid = product_1_valid.text
price_product_1_valid = driver.find_element(By.XPATH, "//div[@class='inventory_item_price'][1]")
value_price_product_1_valid = price_product_1_valid.text
assert value_product_1 == value_product_1_valid
assert value_price_product_1 == value_price_product_1_valid
finish_bt = driver.find_element(By.XPATH, "//button[@id='finish']")
action.move_to_element(finish_bt).perform()
finish_bt.click()
good_test = driver.find_element(By.XPATH, "//h2[@class='complete-header']")
action.move_to_element(good_test).perform()
a = good_test.text
b = 'THANK YOU FOR YOUR ORDER'
assert a == b
print('All GOOD KOLKA ! TEST IS PASSED !')
