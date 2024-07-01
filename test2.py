from selenium import webdriver  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

import os
import time
from datetime import datetime


def test2():
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)

    driver.get(' https://demo.dealsdray.com')

    
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "css-l8vkz1"))
    )

    userName = driver.find_element(By.CLASS_NAME, "css-l8vkz1")
    userName.send_keys('prexo.mis@dealsdray.com')

    password = driver.find_element(By.CLASS_NAME, 'css-r71t31')
    password.send_keys('prexo.mis@dealsdray.com')

    login_btn = driver.find_element(By.CLASS_NAME, "css-1usxxvf")
    login_btn.click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "css-1s178v5"))
    )

    order_btn = driver.find_element(By.CLASS_NAME, "css-1s178v5")
    order_btn.click()

    try:
        orders_btn = driver.find_element(
            By.XPATH, "//a[@href='/mis/orders']//button[.//span[text()='Orders']]")

        orders_btn.click()
    except:
        print('button not pressed')

    window_size = driver.get_window_size()
    current_window = window_size['width']
    if current_window < 1199:
        clickscrn = driver.find_element(By.CLASS_NAME, 'css-1scr8os')
        clickscrn.click()

    try:
        add_bulk_order = driver.find_element(By.CLASS_NAME, "css-vwfva9")
        add_bulk_order.click()
    except:
        print('add btn not clicked')

    file_to_upload = os.path.join(os.getcwd(), 'demo-data.xlsx')
    print(file_to_upload)

    try:

        file_input = driver.find_element(By.TAG_NAME, "input")
        if file_input.get_attribute('type') == 'file':

            file_input.send_keys(
                "C:\\Users\\hasan\\Desktop\\automation\\test2\\demo-data.xlsx")
            print('file uploaded')

    except:
        print('file not uploaded')

    driver.implicitly_wait(1)

    import_btn = driver.find_element(By.CLASS_NAME, "css-6aomwy")
    import_btn.click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

    validate_btn = driver.find_element(By.CLASS_NAME, "css-6aomwy")

    validate_btn.click()
    print('vali btn clicked')

    time.sleep(2)
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert

        alert.accept()
        print('alert clicked')
    except:
        print("btn not pressed")
        pass

    time.sleep(2)
    folder_name = 'screenshots'

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    now = datetime.now().strftime("%D-%M-%Y_%H-%M-%S")

    filename = f"{folder_name}/{now}.png"

    driver.get_screenshot_as_file(filename)

    driver.quit()


test2()
