import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv

load_dotenv()
driver_path = os.getenv('DRIVER_PATH')
proxy_host = os.getenv('PROXY_HOST')
proxy_port = os.getenv('PROXY_PORT')
user_agent = os.getenv('USER_AGENT')

#Инициализация драйвера браузера
@pytest.fixture(scope="module")
def chrome_driver():
    service = Service(executable_path=driver_path)

    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server={}:{}'.format(proxy_host, proxy_port))
    options.add_argument('--user-agent={}'.format(user_agent))
    options.add_argument('--disable-infobars')
    options.add_argument("--disable-blink-features=AutomationControlled")
    #options.add_argument("--headless")

    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    yield driver

    driver.close()
    driver.quit()