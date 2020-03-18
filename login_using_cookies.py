

import pickle
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import time


cpath = "/usr/local/bin/geckodriver"


with webdriver.Firefox(executable_path=cpath) as driver:
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

    # Upload function should come here

    upload_div_class = "input[type='file']"
    # TODO : what if there are many

    file_upload_input = driver.find_element_by_css_selector(upload_div_class)
    lesson_name_input = WebDriverWait(
        driver, 20).until(
        EC.presence_of_element_located(
            (By.ID, "txtLessonName")))
    lesson_name_input.send_keys('Test-File')
    lesson_tags_input = driver.find_element(
        By.CLASS_NAME, "ms-BasePicker-input")
    lesson_tags_input.send_keys('test')
    lesson_tags_input.send_keys(Keys.RETURN)

    absolute_file_path = os.path.abspath('./demo-loggin.mov')
    upload_div_file_name = driver.find_element(
        By.CLASS_NAME, "fileuploadlist").find_elements_by_tag_name("li")[0]
    file_upload_input.send_keys(absolute_file_path)
    # TODO : to be updated to take automatically
    driver.execute_script(
        "arguments[0].innerText = 'demo-loggin.mov'",
        upload_div_file_name)
    save_button = WebDriverWait(
        driver, 20).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[title='Save Lesson']")))
    ActionChains(driver).move_to_element(save_button).click().perform()
    # TODO : this can be improved with a good time  out
    WebDriverWait(
        driver,
        24 *
        60 *
        60).until(
        EC.invisibility_of_element_located(
            (By.CLASS_NAME,
             "bg-Overlap")))
    time.sleep(120)
