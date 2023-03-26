import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

#Тест на открытие "Context Menu"
def test_open_basic_auth(chrome_driver: webdriver):
    chrome_driver.get('http://the-internet.herokuapp.com/')
    link_elements = "http://the-internet.herokuapp.com/context_menu"
    
    link = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/ul/li[7]/a[text()="Context Menu"]'))
    )
    link.click()

    assert link_elements in chrome_driver.current_url

#Тест корректности заголовка
def test_correct_title(chrome_driver: webdriver):

    chrome_driver.get('http://the-internet.herokuapp.com/context_menu')

    correct_title = "Context Menu"

    title = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/h3')) 
    )

    assert title.text == correct_title