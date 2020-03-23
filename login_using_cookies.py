import pickle
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from constants import DRIVER_PATH
from actions.admin_panel import (click_profile_button,
                                 click_view_as_admin,
                                 send_subject_title,
                                 send_subject_tag,
                                 )
from actions.login import login_using_cookies
from actions.file_upload import upload_file


with webdriver.Chrome(DRIVER_PATH) as driver:
    login_using_cookies(driver)
    click_profile_button(driver)
    click_view_as_admin(driver)
    # Upload function should come here
    # TODO : what if there are many
    send_subject_title(driver, 'test-file')
    send_subject_tag(driver, 'test')
    upload_file(driver, './move.mov')  # to be changed
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
