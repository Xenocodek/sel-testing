import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Тест на открытие "Checkboxes"
def test_open_checkboxes(chrome_driver: webdriver):
    chrome_driver.get('http://the-internet.herokuapp.com/')
    link_elements = "http://the-internet.herokuapp.com/checkboxes"
    
    link = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/ul/li[6]/a[text()="Checkboxes"]'))
    )
    link.click()

    assert link_elements in chrome_driver.current_url

#Тест корректности заголовка
def test_correct_title(chrome_driver: webdriver):

    chrome_driver.get('http://the-internet.herokuapp.com/checkboxes')

    correct_title = "Checkboxes"

    title = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/h3')) 
    )

    assert title.text == correct_title