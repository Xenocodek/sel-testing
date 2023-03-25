import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

#Тест на открытие "Basic Auth"
def test_open_basic_auth(chrome_driver: webdriver):
    chrome_driver.get('http://the-internet.herokuapp.com/')
    link_elements = "http://the-internet.herokuapp.com/basic_auth"
    
    link = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/ul/li[3]/a[text()="Basic Auth"]'))
    )
    link.click()

    assert link_elements in chrome_driver.current_url

#Тест успешной авторизации
def test_successfull_auth(chrome_driver: webdriver):
    username = 'admin'
    password = 'admin'
    correct_title = "Basic Auth"
    correct_description = "Congratulations! You must have the proper credentials."

    url = f'http://{username}:{password}@the-internet.herokuapp.com/basic_auth'

    chrome_driver.get(url)

    title = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/h3')) 
    )

    assert title.text == correct_title

    description = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/p'))
    )

    assert description.text == correct_description

#Тест авторизации с неправильным логином и паролем
def test_incorrect_login_password(chrome_driver: webdriver):
    username = 'user'
    password = 'user'

    url = f'http://{username}:{password}@the-internet.herokuapp.com/basic_auth'

    chrome_driver.get(url)

    assert url in chrome_driver.current_url

#Тест авторизации с неправильным логином
def test_incorrect_login(chrome_driver: webdriver):
    username = 'user'
    password = 'admin'

    url = f'http://{username}:{password}@the-internet.herokuapp.com/basic_auth'

    chrome_driver.get(url)

    assert url in chrome_driver.current_url

#Тест авторизации с неправильным паролем
def test_incorrect_password(chrome_driver: webdriver):
    username = 'admin'
    password = 'user'

    url = f'http://{username}:{password}@the-internet.herokuapp.com/basic_auth'

    chrome_driver.get(url)

    assert url in chrome_driver.current_url