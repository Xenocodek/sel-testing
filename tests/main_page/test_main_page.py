import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Тест на открытие главной страницы
def test_open_main_page(chrome_driver: webdriver):
    chrome_driver.get('http://the-internet.herokuapp.com/')
    assert "The Internet" in chrome_driver.title

#Тест на присутствия приветствия на странице
def test_on_welcome(chrome_driver: webdriver):
    chrome_driver.get('http://the-internet.herokuapp.com/')

    welcome_text = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/h1'))
    )

    assert welcome_text.text == "Welcome to the-internet"

#Тест на отображение ссылок
def test_display_links(chrome_driver: webdriver):
    chrome_driver.get('http://the-internet.herokuapp.com/')

    links = chrome_driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        assert link.is_displayed()