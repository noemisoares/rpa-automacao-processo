from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def realizar_login():
    print(">>> LOGIN INICIADO <<<")

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    print(">>> LOGIN FINALIZADO <<<")
    return driver
