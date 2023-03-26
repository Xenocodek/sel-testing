import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Тест на открытие "Digest Auth"
def test_open_digest_auth(chrome_driver: webdriver):
    chrome_driver.get('http://the-internet.herokuapp.com/')
    link_elements = "http://the-internet.herokuapp.com/digest_auth"
    
    link = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/ul/li[8]/a[text()="Digest Authentication"]'))
    )
    link.click()

    assert link_elements in chrome_driver.current_url