

import pickle
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
from utils import find_by_css, find_element_by_name


cpath = "/usr/local/bin/chromedriver"


with webdriver.Chrome(cpath) as driver:
    driver.get('https://unictmob.azurewebsites.net/')
    for cookie in pickle.load(open("web-cookies.pkl", "rb")):
        if 'expiry' in cookie:
            del cookie['expiry']
        driver.add_cookie(cookie)
    driver.get('https://unictmob.azurewebsites.net/')
    profile_button = driver.find_element(By.ID, "Profile")
    profile_button.click()
    view_as_admin_locator = 'menu-item-Generic_View_Admin'
    code_validate_button = driver.find_element(By.ID, view_as_admin_locator)
    code_validate_button.click()
    # trying to click the upload bluk
    view_more_button = WebDriverWait(
        driver, 20).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[title='More']")))
    view_more_button.click()

    bluk_download_button = WebDriverWait(
        driver, 20).until(
        EC.element_to_be_clickable(
            (By.NAME, "Bulk upload courses")))

    bluk_download_button.click()

    # simulating download

    select_file_button = WebDriverWait(
        driver, 20).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[aria-label='Browse']")))

    driver.execute_script(
        "HTMLInputElement.prototype.click = function() {if(this.type !== 'file') HTMLElement.prototype.click.call(this);};")
    select_file_button.click()

    absolute_file_path = os.path.abspath('1584537484.023008.zip')

    select_file_input = driver.find_element(
        By.CSS_SELECTOR, "input[type=file]")
    select_file_input.send_keys(absolute_file_path)
    WebDriverWait(
        driver,
        24 *
        60 *
        60).until(
        EC.invisibility_of_element_located(
            (By.CLASS_NAME,
             "bg-Overlap")))
    time.sleep(120)
