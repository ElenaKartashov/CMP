from selenium import webdriver
import time
import os
import StringIO
import sys
import csv, sys
import urlparse
import xlrd
import pandas
#import pytest
#import allure
pytest_plugins = 'allure.pytest_plugin'
import HTMLTestRunner
import unittest
import Images
from selenium.webdriver.support.ui import WebDriverWait


WebDriverWait = (10)


driver = webdriver.Chrome("/Users/Lena/PycharmProjects/First_selenium_test/drivers/chromedriver")
base_url = ('https://primary_link.com')

driver.set_page_load_timeout(20)

driver.get("https://primary_link.com")


def waitElementPresentByCss (timeout, numberAttempts, elementCss):
    if numberAttempts!=0:
        time.sleep(timeout)
        print "Debug: attempt number " + str(numberAttempts)
    else: return

    print elementCss
    try:
        elm = driver.find_element_by_css_selector(elementCss)
        if elm.is_displayed()!=True:
            waitElementPresentByCss(timeout, numberAttempts-1, elementCss)
        print "Debug: Try block"
    except:
        waitElementPresentByCss(timeout, numberAttempts - 1, elementCss)
        print "Debug: except block"


waitElementPresentByCss (3, 3, '#LearnMore[href*="/cash-back-credit-cards/chase-freedom-unlimited"]')

driver.find_element_by_css_selector('#LearnMore[href*="/unlimited"]').click()
#driver.find_element_by_css_selector('#LearnMore[href*="/balance"]').click()
driver.back()
time.sleep(4)
driver.forward()

time.sleep(4)
driver.quit()
