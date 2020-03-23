from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def click_login_button(driver):
    """
    Perform click to the login button
    Args:
        driver ([type]): link to chrome driver
    """
    login_element = driver.find_element(
        By.CLASS_NAME, "header__signing-button")
    login_element.click()


def input_the_number(driver):
    """
    Perform enter phone number action
    Args:
        driver : the web driver
    """
    country_select_button = Select(
        driver.find_element(
            By.CLASS_NAME,
            "react-phone-number-input__country-select"))
    country_select_button.select_by_visible_text('Rwanda')
    input_phone_element = driver.find_element(
        By.CLASS_NAME, "react-phone-number-input__input")
    input_phone_element.send_keys('784834836')
    phone_validate_button = driver.find_element(
        By.CLASS_NAME, "ms-Button--primary")
    phone_validate_button.click()


def validate_phone_number(driver):
    """
    validate the OTP code send on the phone number
    Args:
        driver ([type]): chrome driver
    """
    code = input("Enter The code you got on your phone : ")
    code_input_element = driver.find_element(By.NAME, "OTP")
    code_validate_button = driver.find_element(
        By.CLASS_NAME, "ms-Button-label")
    code_input_element.send_keys(str(code))
    code_validate_button.click()
