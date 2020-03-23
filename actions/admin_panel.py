from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def click_profile_button(driver):
    """
    Perform click to the profile button
    Args:
        driver ([type]): chrome web driver
    """
    profile_button = driver.find_element(By.ID, "Profile")
    profile_button.click()


def click_view_as_admin(driver):
    """
    Perform click to view as admin function
    Args:
        driver ([type]): chrome web driver
    """
    view_as_admin_locator = 'menu-item-Generic_View_Admin'
    code_validate_button = driver.find_element(By.ID, view_as_admin_locator)
    code_validate_button.click()


def send_subject_title(driver, name):
    """
    Perform send subject title
    Args:
        driver ([type]): chrome web driver
        name (String) : the lesson name input
    """
    lesson_name_input = WebDriverWait(
        driver, 20).until(
        EC.presence_of_element_located(
            (By.ID, "txtLessonName")))
    lesson_name_input.send_keys(name)


def send_subject_tag(driver, tag):
    """
    send subject tags
    Args:
        driver ([type]): chrome web driver
        tag (string): tag to send
    """
    lesson_tags_input = driver.find_element(
        By.CLASS_NAME, "ms-BasePicker-input")
    lesson_tags_input.send_keys(tag)
    lesson_tags_input.send_keys(Keys.RETURN)


def click_view_more(driver):
    """
    perform click to the view more button
    Args:
        driver ([type]): [description]
    """
    view_more_button = WebDriverWait(
        driver, 20).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[title='More']")))
    view_more_button.click()


def click_bluk_upload(driver):
    bluk_download_button = WebDriverWait(
        driver, 20).until(
        EC.element_to_be_clickable(
            (By.NAME, "Bulk upload courses")))
    bluk_download_button.click()
