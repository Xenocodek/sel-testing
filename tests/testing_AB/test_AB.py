import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Тест на открытие "A/B Test"
def test_open_AB(chrome_driver: webdriver):
    chrome_driver.get('http://the-internet.herokuapp.com/')
    link_AB = "http://the-internet.herokuapp.com/abtest"
    
    link = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/ul/li[1]/a[text()="A/B Testing"]'))
    )
    link.click()

    assert link_AB in chrome_driver.current_url

#Тест вариаций A/B заголовка
def test_correct_title(chrome_driver: webdriver):

    version_A = "A/B Test Variation 1"
    version_B = "A/B Test Control"

    title = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/h3'))
    )

    assert title.text == version_A or title.text == version_B

#Тест описания вариации A/B
def test_ab_description(chrome_driver: webdriver):
    
    description_A = "Also known as split testing. This is a way in which businesses are able " \
    "to simultaneously test and learn different versions of a page to " \
    "see which text and/or functionality works best towards a desired outcome " \
    "(e.g. a user action such as a click-through)."

    description_B = "Also known as split testing. This is a way in which businesses are able " \
    "to simultaneously test and learn different versions of a page to " \
    "see which text and/or functionality works best towards a desired outcome " \
    "(e.g. a user action such as a click-through)."

    description = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/p'))
    )

    assert description.text == description_A or description.text == description_B