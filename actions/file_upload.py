import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def upload_file(driver, file_path):
    """
    Perform file upload_action
    Args:
        driver ([type]): chrome web driver
        file_path (string): file path
    """
    absolute_file_path = os.path.abspath(file_path)
    file_name = os.path.basename(absolute_file_path)
    upload_div_class = "input[type='file']"
    file_upload_input = driver.find_element_by_css_selector(upload_div_class)
    upload_div_file_name = driver.find_element(
        By.CLASS_NAME, "fileuploadlist").find_elements_by_tag_name("li")[0]
    file_upload_input.send_keys(absolute_file_path)
    driver.execute_script(
        f"arguments[0].innerText = '{file_name}'",
        upload_div_file_name)
    save_button = WebDriverWait(
        driver, 20).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[title='Save Lesson']")))
    ActionChains(driver).move_to_element(save_button).click().perform()


def upload_zip(driver, path):
    """
    perform zip file upload
    
    Args:
        driver (): 
        path ([type]): [description]
    """
    select_file_button = WebDriverWait(
        driver, 20).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[aria-label='Browse']")))

    driver.execute_script(
        "HTMLInputElement.prototype.click = function() {if(this.type !== 'file') HTMLElement.prototype.click.call(this);};")
    select_file_button.click()

    absolute_file_path = os.path.abspath(path)

    select_file_input = driver.find_element(
        By.CSS_SELECTOR, "input[type=file]")
    select_file_input.send_keys(absolute_file_path)
