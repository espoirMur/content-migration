from selenium.webdriver.common.by import By


def find_by_css(driver, element):
    """
    Find element by css

    Args:
        driver ([type]): [description]
        element ([type]): [description]
    """
    return driver.find_element(By.CLASS_NAME, element)


def find_element_by_name(driver, element):
    """
    FInd element by name

    Args:
        driver ([type]): [description]
        element ([type]): [description]
    """
    return driver.find_element(By.NAME, element)
