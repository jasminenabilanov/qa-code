from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from dotenv import load_dotenv
load_dotenv()


@given('Access URL Gist')
def step(driver):
   driver.browser.get('https://gist.github.com/')
   time.sleep(2)
   driver.browser.maximize_window()
   time.sleep(2)

@when('Fill username and password git')
def step(driver):
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

@when('Fill description gist')
def step(driver):
    driver.browser.find_element_by_name("gist[description]").send_keys("gist description")
    time.sleep(2)

@when('Fill filename including extension')
def step(driver):
    driver.browser.find_element_by_name("gist[contents][][name]").send_keys("testqa.py")
    time.sleep(2)

@when('Fill description text area')
def step(driver):
    driver.browser.find_element_by_xpath("//pre[contains(@class,'CodeMirror-line')]").send_keys("ini hanya contoh dari deskripsi saja")
    time.sleep(2)

@when('click button submit')
def step(driver):
    driver.browser.find_element_by_xpath("//button[contains(text(),'Create public gist')]").click()
    time.sleep(1)

@then('I should see successfully')
def step(driver):
    label_text_created_now = driver.browser.find_element_by_xpath("//h1[@class='public css-truncate float-none flex-auto width-fit pl-0']")
    print("SUCCESS !!!")