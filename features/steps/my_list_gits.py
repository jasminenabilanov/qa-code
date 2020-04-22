from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv
load_dotenv()


@given('Login gits to see my list')
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

@then('click see all my gits and should be successfully')
def step(driver):
   driver.browser.find_element_by_xpath("//a[contains(text(),'See all of your gists')]").click()
   time.sleep(2)
   see_all_gits = driver.browser.find_element_by_xpath("//div[@class='col-9']")
   print(see_all_gits)



    
    