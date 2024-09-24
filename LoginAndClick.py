from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

def get_driver() :
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximised")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    # https://automated.pythonanywhere.com
    # https://automated.pythonanywhere.com/login/
    # /html/body/div[1]/div/div/div[3]/form/button
    # /html/body/nav/div/a

    driver.get("https://automated.pythonanywhere.com/login/")
    return driver

def clean_text (text) :
    return float (text.split(":")[1])

def main() :
    driver = get_driver()
    time.sleep(2)
    driver.find_element(By.ID, "id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(By.ID, "id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/nav/div/a").click()
    time.sleep(2)
    dyanmic_element = driver.find_element(By.ID, "displaytimer")
    return clean_text(dyanmic_element.text)

print(main())