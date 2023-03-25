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

#Тест корректности заголовка
def test_correct_title(chrome_driver: webdriver):

    correct_title = "Add/Remove Elements"

    title = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/h3')) 
    )

    assert title.text == correct_title

#Тест кнопки добавления элемента
def test_add_element(chrome_driver: webdriver):

    button_add = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/button[text()="Add Element"]'))
    )

    button_add.click()

    button_delete = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="elements"]/button[text()="Delete"]'))
    )

    assert button_delete is not None

#Тест кнопки удаления элемента
def test_remove_element(chrome_driver: webdriver):

    button_delete = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="elements"]/button[text()="Delete"]'))
    )

    button_delete.click()

    button_remove = WebDriverWait(chrome_driver, 10).until(
        EC.staleness_of(button_delete)
    )

    assert button_remove

#Тест добавления и удаления кнопок
def test_add_remove_elements(chrome_driver: webdriver):

    button_add = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/button[text()="Add Element"]'))
    )

    for i in range(9):
        button_add.click()

    while True:
        button_delete = WebDriverWait(chrome_driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'added-manually'))
        )
        button_delete.click()

        button_remove = WebDriverWait(chrome_driver, 10).until(
        EC.staleness_of(button_delete)
        )

        if button_remove:
            break

    assert button_remove