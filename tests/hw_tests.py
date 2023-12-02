import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By



def test_menu_1(driver_my):
    top_menu_item_1 = driver_my.find_element(By.ID, 'ui-id-3')
    top_menu_item_1.click()
    time.sleep(2)
    target_button = driver_my.find_element(By.XPATH, '/html/body/div[2]/main/div[4]/div[1]/div[1]/div[1]/a/span/span[2]')
    assert target_button.is_enabled()

def test_menu_2(driver_my):
    top_menu_item_2 = driver_my.find_element(By.ID, 'ui-id-4')
    action = ActionChains(driver_my)
    action.move_to_element(top_menu_item_2)
    time.sleep(1)
    tops = driver_my.find_element(By.ID, 'ui-id-9')
    action.click(tops)
    time.sleep(1)
    action.perform()
    color_option = driver_my.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div[2]/div/div[2]/div/div[5]/div[1]')
    assert color_option.is_enabled()

def test_menu_3(driver_my):
    top_menu_item_3 = driver_my.find_element(By.ID, 'ui-id-5')
    action = ActionChains(driver_my)
    action.move_to_element(top_menu_item_3)
    time.sleep(1)
    tops = driver_my.find_element(By.ID, 'ui-id-17')
    action.move_to_element(tops)
    time.sleep(1)
    bottoms = driver_my.find_element(By.ID, 'ui-id-18')
    action.move_to_element(bottoms)
    action.perform()
    assert bottoms.is_enabled()
