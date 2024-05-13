import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://ukr.net')
text_box = driver.find_element(By.XPATH, "//a[text() = 'Війна']/../..")
print(text_box.text)

driver_1 = webdriver.Chrome()
driver_1.get('https://www.google.com/')
links = driver_1.find_elements(By.TAG_NAME, 'a')
for link in links:
    print(link.get_attribute('href'))
driver_1.get('https://mail.google.com/mail/&ogbl')
driver_1.back()
driver_1.get('https://www.google.com/imghp?hl=ru&ogbl')
driver_1.back()

driver_2 = webdriver.Chrome()
driver_2.get('https://magento.softwaretestingboard.com')
menu = driver_2.find_element(By.PARTIAL_LINK_TEXT, 'Men')
menu.click()
submenu = driver_2.find_element(By.PARTIAL_LINK_TEXT, 'Tops')
action =ActionChains(driver_2)
submenu_items = driver_2.find_element(By.PARTIAL_LINK_TEXT, 'Jackets')
action.move_to_element(submenu)
action.click(submenu_items)
action.perform()

driver_3 = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome(options=chrome_options)
driver_3.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
drag = WebDriverWait(driver_3, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[starts-with(@id, "box") and text()="Rome"]')))
drop = WebDriverWait(driver_3, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[starts-with(@id, "box") and text()="Italy"]')))
ActionChains(driver_3).drag_and_drop(drag, drop).perform()
