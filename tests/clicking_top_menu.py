import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://magento.softwaretestingboard.com/')
wait = WebDriverWait(driver,10)
top_menu_item_1 = wait.until(EC.element_to_be_clickable((By.ID, 'ui-id-3')))
top_menu_item_1.click()
top_menu_item_2 = driver.find_element(By.ID, 'ui-id-4')
top_menu_item_2.click()
top_menu_item_3 = driver.find_element(By.ID, 'ui-id-5')
top_menu_item_3.click()
top_menu_item_4 = driver.find_element(By.ID, 'ui-id-6')
top_menu_item_4.click()
top_menu_item_5 = driver.find_element(By.ID, 'ui-id-7')
top_menu_item_5.click()
top_menu_item_6 = driver.find_element(By.ID, 'ui-id-8')
top_menu_item_6.click()
