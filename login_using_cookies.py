

import pickle
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

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

    ## Upload function should come here

    save_button = driver.find_element_by_css_selector("[title^='Save Lesson']")

    upload_div_class = "input[type='file']"
    file_upload_input = driver.find_element_by_css_selector(upload_div_class)

    lesson_name_input = driver.find_element(By.ID, "txtLessonName")
    lesson_name_input.send_keys('Test-File')
    lesson_tags_input = driver.find_element(By.CLASS_NAME, "ms-BasePicker-input")
    lesson_tags_input.send_keys('test')
    lesson_tags_input.send_keys(Keys.RETURN)
    
    absolute_file_path = os.path.abspath('./download_files_from_jupyter.mov')
    file_upload_input.send_keys(absolute_file_path)
    
    save_button.click()

