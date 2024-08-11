from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
from PIL import Image

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://demo.dealsdray.com')
    userName = driver.find_element(By.CLASS_NAME, "css-l8vkz1")
    userName.send_keys('prexo.mis@dealsdray.com')

    password = driver.find_element(By.CLASS_NAME, 'css-r71t31')
    password.send_keys('prexo.mis@dealsdray.com')

    try:
        login_btn = driver.find_element(By.CLASS_NAME, "css-1usxxvf")
        login_btn.click()

    except:
        print('didnt click the btn')

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
        print(current_window)

    try:
        add_bulk_order = driver.find_element(By.CLASS_NAME, "css-vwfva9")
        add_bulk_order.click()
    except:
        print('add btn not clicked')

    time.sleep(2)

    try:
        hamburgerbtn = driver.find_element(By.XPATH, "//span[@class='material-icons notranslate MuiIcon-root MuiIcon-fontSizeMedium css-1jgtvd5']")
        hamburgerbtn.click()
    except:
      print('not clicked the hambtn')

    try:
        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
        file_input = driver.find_element(By.TAG_NAME, "input")
        if file_input.get_attribute('type') == 'file':
            file_input.send_keys(r"C:\Users\hasan\Desktop\dealsdray\demo-data.xlsx")
            print('file uploaded')

    except:
        print('file not uploaded')
    
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
        return
    
    driver.save_screenshot('ss.png')
    screenshot = Image.open('ss.png')
    screenshot.show()
    time.sleep(2)
    
    driver.quit()

if __name__ =="__main__":
    main()


