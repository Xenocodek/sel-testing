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

    welcome_text = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/h1'))
    )

    assert welcome_text.text == "Welcome to the-internet"

#Тест на отображение ссылок
def test_display_links(chrome_driver: webdriver):

    links = chrome_driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        assert link.is_displayed()

#Тест на наличие футера
def test_display_footer(chrome_driver: webdriver):

    footer_text_1 = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="page-footer"]/div/div[text()="Powered by "]'))
    )
    assert footer_text_1 is not None

    footer_text_2 = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="page-footer"]/div/div/a[text()="Elemental Selenium"]'))
    )
    assert footer_text_2 is not None

#Тест на наличие картинки
def test_display_img(chrome_driver: webdriver):

    img_element = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/a/img[@src="/img/forkme_right_green_007200.png"]'))
    )

    assert img_element.get_attribute("src") == 'http://the-internet.herokuapp.com/img/forkme_right_green_007200.png'