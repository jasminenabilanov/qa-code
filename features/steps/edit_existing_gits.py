from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time, datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv()


@given('Log in as user to access gits')
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

@when('click button see all gits to edit')
def step(driver):
    driver.browser.find_element_by_xpath("//a[contains(text(),'See all of your gists')]").click()
    time.sleep(2)

@when('choose one gits to edit')
def step(driver):
    driver.browser.find_element_by_xpath("//td[@id='file-testqa-py-LC1']").click()
    time.sleep(1)

@when('click button edit gits')
def step(driver):
    driver.browser.find_element_by_xpath("//body[@class='logged-in env-production min-width-lg']/div[contains(@class,'application-main')]/div/main[@id='gist-pjax-container']/div[@class='gisthead pagehead repohead readability-menu bg-gray-light pb-0 pt-3 mb-4']/div[@class='container-lg px-3']/div[@class='mb-3 d-flex']/ul[@class='pagehead-actions float-none']/li/a[1]").click()
    time.sleep(1)

@when('Edit text area')
def step(driver):
    driver.browser.find_element_by_xpath("//pre[contains(@class,'CodeMirror-line')]").clear()
    time.sleep(2)
    driver.browser.find_element_by_xpath("//pre[contains(@class,'CodeMirror-line')]").click()
    driver.browser.find_element_by_xpath("//pre[contains(@class,'CodeMirror-line')]").send_keys("ini deskripsi yang sudah di edit")

@when('click button update public gist')
def step(driver):
    driver.browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()

@then('i should be successfully edit gits')
def step(driver):
    label_text_created_now = driver.browser.find_element_by_xpath("//h1[@class='public css-truncate float-none flex-auto width-fit pl-0']")
    print("SUCCESS EDIT !!!")








