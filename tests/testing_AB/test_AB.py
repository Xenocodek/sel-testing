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