from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from dotenv import load_dotenv
load_dotenv()

@given('Log in as user to delete gits')
def step(driver):
    driver.browser.get('https://gist.github.com/')
    time.sleep(2)
    driver.browser.maximize_window()
    time.sleep(2)

    driver.browser.find_element_by_xpath("//a[@class='HeaderMenu-link no-underline mr-3']").click()
    time.sleep(2)
    secret_username = os.getenv("EMAIL")
    secret_password = os.getenv("PASS")

    login = driver.browser.find_element_by_id('login_field').send_keys(secret_username)
    time.sleep(2)
    password = driver.browser.find_element_by_id('password').send_keys(secret_password)
    time.sleep(2)
    driver.browser.find_element_by_xpath("//input[@name='commit']").click()

    driver.browser.get('https://gist.github.com/')

@when('click button see all gits')
def step(driver):
    driver.browser.find_element_by_xpath("//a[contains(text(),'See all of your gists')]").click()
    time.sleep(2)

@when('choose gits to delete')
def step(driver):
    driver.browser.find_element_by_xpath("//td[@id='file-testqa-py-LC1']").click()
    time.sleep(1)

@when('click button delete')
def step(driver):
    driver.browser.find_element_by_xpath("//button[@class='btn btn-sm btn-danger']").click()
    alert = driver.browser.switch_to.alert
    alert.accept()

@then('i should be successfully deleted')
def step(driver):
    time.sleep(2)
    label_delete = driver.browser.find_element_by_xpath("//div[contains(@class,'flash flash-full flash-notice')]")
    if label_delete.text == 'Gist deleted successfully':
        print("-> Delete success")
        assert True is not False
    else:
        print("-> Oops, Something went wrong")
        raise Exception
    