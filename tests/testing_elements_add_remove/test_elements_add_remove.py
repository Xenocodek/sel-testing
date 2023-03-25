import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Тест на открытие "Add/Remove Elements"
def test_open_elements_add_remove(chrome_driver: webdriver):
    chrome_driver.get('http://the-internet.herokuapp.com/')
    link_elements = "http://the-internet.herokuapp.com/add_remove_elements/"
    
    link = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/ul/li[2]/a[text()="Add/Remove Elements"]'))
    )
    link.click()

    assert link_elements in chrome_driver.current_url