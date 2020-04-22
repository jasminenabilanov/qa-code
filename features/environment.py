from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


def before_all(driver):
	driver.browser = webdriver.Chrome()
	

def after_all(driver):
	driver.browser.quit()