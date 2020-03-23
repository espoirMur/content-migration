import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from actions.admin_panel import (click_profile_button,
                                 click_view_as_admin,
                                 click_view_more,
                                 click_bluk_upload)
from actions.login import login_using_cookies
from constants import DRIVER_PATH
from actions.file_upload import upload_zip


with webdriver.Chrome(DRIVER_PATH) as driver:
    login_using_cookies(driver)
    click_profile_button(driver)
    click_view_as_admin(driver)
    # trying to click the upload bluk
    click_view_more(driver)
    click_bluk_upload(driver)
    # simulating download
    upload_zip(driver, '1584537484.023008.zip')
    WebDriverWait(
        driver,
        24 *
        60 *
        60).until(
        EC.invisibility_of_element_located(
            (By.CLASS_NAME,
             "bg-Overlap")))
    time.sleep(120)
