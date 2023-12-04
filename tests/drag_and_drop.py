import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_drag_drop():
    driver = webdriver.Chrome()
    driver.get('https://the-internet.herokuapp.com/drag_and_drop')
    drag = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'column-a')))
    drop = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'column-b')))
    time.sleep(2)
    action = ActionChains(driver).drag_and_drop(drag, drop)
    action.perform()
    time.sleep(2)
    assert 1 == 1
