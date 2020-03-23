from selenium import webdriver
import pickle
from constants import DRIVER_PATH, LOGIN_URL
from actions.login import click_login_button,  input_the_number, validate_phone_number

driver = None

try:
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(LOGIN_URL)
    click_login_button(driver)
    input_the_number(driver)
    validate_phone_number(driver)
    driver.get(LOGIN_URL)
    pickle.dump(driver.get_cookies(), open("web-cookies.pkl", "wb"))
finally:
    if driver is not None:
        driver.close()
