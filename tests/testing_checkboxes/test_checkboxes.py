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

    correct_title = "Checkboxes"

    title = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/h3')) 
    )

    assert title.text == correct_title

#Тест на отобрежение чекбоксов по умолчанию
def test_default_checkboxes(chrome_driver: webdriver):

    checkbox_1 = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="checkboxes"]/input[1]'))
    )

    assert not checkbox_1.is_selected()

    checkbox_2 = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="checkboxes"]/input[2]'))
    )

    assert checkbox_2.is_selected()

#Тест на пустые чекбоксы
def test_empty_checkboxes(chrome_driver: webdriver):

    checkbox_1 = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="checkboxes"]/input[1]'))
    )

    assert not checkbox_1.is_selected()

    checkbox_2 = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="checkboxes"]/input[2]'))
    )

    checkbox_2.click()

    assert not checkbox_2.is_selected()

#Тест на отмеченные чекбоксы
def test_selected_checkboxes(chrome_driver: webdriver):

    chrome_driver.get('http://the-internet.herokuapp.com/checkboxes')

    checkbox_1 = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="checkboxes"]/input[1]'))
    )

    checkbox_1.click()

    assert checkbox_1.is_selected()

    checkbox_2 = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="checkboxes"]/input[2]'))
    )

    assert checkbox_2.is_selected()