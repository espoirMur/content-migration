from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pickle

LOGIN_URL = "https://unictmob.azurewebsites.net/"
driver = None

try:
    cpath = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(cpath)
    driver.get(LOGIN_URL)
    login_element = driver.find_element(By.CLASS_NAME, "header__signing-button")
    login_element.click()
    country_select_button = Select(driver.find_element(By.CLASS_NAME, "react-phone-number-input__country-select"))
    country_select_button.select_by_visible_text('Rwanda')
    input_phone_element = driver.find_element(By.CLASS_NAME, "react-phone-number-input__input")
    input_phone_element.send_keys('784834836')
    phone_validate_button = driver.find_element(By.CLASS_NAME, "ms-Button--primary")
    phone_validate_button.click()
    code = input("Enter The code you got on your phone : ")
    code_input_element = driver.find_element(By.NAME, "OTP")
    code_validate_button = driver.find_element(By.CLASS_NAME, "ms-Button-label")
    code_input_element.send_keys(str(code))
    code_validate_button.click()
    driver.get('https://unictmob.azurewebsites.net/')
    pickle.dump(driver.get_cookies(), open("web-cookies.pkl", "wb"))
finally:
    if driver is not None:
        driver.close()
