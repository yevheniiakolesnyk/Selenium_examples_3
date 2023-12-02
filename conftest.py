import time
import pytest
from selenium import webdriver

BASE_URL = "https://magento.softwaretestingboard.com/"


@pytest.fixture
def driver_my():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.implicitly_wait(10)
    yield driver
    time.sleep(3)
    driver.quit()
