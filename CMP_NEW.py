# -*- coding: utf-8 -*-
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


#import HTMLTestRunner
#import open_workbook




#def TestRunner (startId, endId)
    #FOR startID to endID
        #VerifyCard(currentTestCaseId)
            #Navigate
            #Find and click correponding card
            #Verify Cell= VerifyURLParam ("https://creditcards.chase.com/all-credit-cards?iCELL=61FY", "Code", "new")
            #VerifySource=VerifyURLParam ("https://creditcards.chase.com/all-credit-cards?iCELL=61FY", "iCELL", "61FY")
            #CompareCards
    #VerifySiteMap - ok
    #VerifyFooterLinks - ok
    #VerifyHeaderLinks - ok
#Universal function to retrieve URL param and compare its value against expected value
#ParamName - url param to verify
#ExpectedParamValue - expected value of the param

browserPath = "/Users/Lena/PycharmProjects/First_selenium_test/drivers/chromedriver"
browserName = "chrome"
environment = "prod"
startId = 1
endId = 3
testCaseFile = "/Users/Lena/PycharmProjects/CMP_NEW/testcases.xlsx"
SheetName = "Sheet1"
Environment="prod"


class CMPsuite (unittest.TestCase):
    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)

    def test_footers(self):
        self.assertTrue(1,1)

    def test_headers (self):
        print "Header passed"
        pass

    def test_navigation (self):
        self.assertEquals(1,1)


    def test_data_driven_CC_Market_Place(self):
        global testCaseFile
        global SheetName
        global startId
        global endId
        global browserName
        global browserPath
        global Environment

        #runner.run(self.suite)
        #with allure.step('step one'):

        #if testCaseFile!="":
        #    testCaseFile=testCaseFile
        #else: testCaseFile="testcases.xlsx"
        #if SheetName!= "":
        #    SheetName = SheetName
        #else: SheetName = "Sheet1"

        TestDataArray = getTestData(testCaseFile, SheetName)
        print TestDataArray
        for id in range (startId, endId+1):

            cur=id-1
            cardName = str(TestDataArray["cardName"][cur])
            cardLocator = str(TestDataArray["cardLocator"][cur])
            locatorValue = str(TestDataArray["locatorValue"][cur])
            curParamName=str(TestDataArray["ParameterCode"][cur])
            curExpectedParamValue = str(TestDataArray["ParameterValue"][cur])
            curParamAlias = str(TestDataArray["ParameterName"][cur])
            startURL=str(TestDataArray["OptionalURL"][cur])
            ExpectedContent = str(TestDataArray["PageContent"][cur])

            scrrenshot = Images.Screenshot()

            if startURL=="" or startURL is None or startURL=="nan":
                startURL="https://creditcards.chase.com"
            print startURL

            print 'Test case for credit card ', cardName, ' has started'
            driver = StartTestCase(startURL, browserName, browserPath, id)

            #driver.getElementByLinkName("cardLocator").click()
            #if driver.getElementByName("cardLName")
                #getElementByLinkName.assertTrue(cardName, realName, )
                #print (cardName " is succeffully opened")
            VerifyURLParam(self, curParamName, curExpectedParamValue, curParamAlias, driver)
            ###navigateTo(self, driver, "data-pt-name", "cc_freedom_ulim_allcc_name")
           #### VerifyPageContent(self, driver, "chaseanalytics-track-link", ExpectedContent)

            last_scr_file_path = scrrenshot.captureScreenshot(driver)
            #else: print ("Card is not found. Test is Failed")

            EndTestCase (driver, id)

def VerifyURLParam (self, ParamName, ExpectedParamValue, ParamAlias, driver):
    try:
        myurl=driver.current_url
        parsed = urlparse.urlparse(myurl)
        urlparse.parse_qs(parsed.query)[ParamName]
        if urlparse.parse_qs(parsed.query)[ParamName]:
            cellCode = urlparse.parse_qs(parsed.query)[ParamName][0]
            #self.assertEqual(cellCode, ExpectedParamValue)
            if cellCode == ExpectedParamValue:
                pass
                print ParamAlias, ' value of current URL is correct = ', str(cellCode)

            else:
                #HTMLTestRunner._TestResult.addSuccess(self, "tests")
                self.fail (ParamAlias + " value of current URL is incorrect Current = " + str(
                    cellCode) + " expected = " + ExpectedParamValue)
    except:
        self.fail("Expected parameter "+ParamName+" of current URL does not have value. Actual URL is  "+myurl)\

def VerifyPageContent (self, driver, locator, ExpectedContent):
    print 'Page verification with ', locator, 'and expected content ', ExpectedContent
    curContent=driver.find_element_by_class_name(locator).text
    curContent = curContent.encode('utf-8')
    #print curContent
    if curContent==ExpectedContent.encode('utf-8'):
        pass
        print "Contect matches expected one"
    else:
        print ("Fail: Current content '"+curContent+"' does not match expected one '"+ExpectedContent)
        #self.fail("Fail: Current content '"+curContent+"' does not match expected one '"+ExpectedContent)

def StartTestCase (url, browserName, browserPath, id):
    print ('Test case number ', id, ' has started')
    defaultBrowserName="chrome"
    defaultBrowserPath = "/Users/Lena/PycharmProjects/First_selenium_test/drivers/chromedriver"
    if browserName == "chrome":
        driver = webdriver.Chrome(browserPath)
    elif browserName == "":
        driver = webdriver.Chrome(defaultBrowserPath)
    driver.set_page_load_timeout(15)
    driver.maximize_window()
    myurlgo=driver.get(url)
    pass
    driver.maximize_window()
    #if environment=="staging":
        #LogIn(UserName, Password)
    return driver

def EndTestCase(driver, id):
    driver.close()
    print 'Test case number ', id, ' has completed'


def getTestData (filePath, Sheet):
    import pandas as pd
    TestDataArray = pd.read_excel(filePath)
    return TestDataArray

####def navigateTo(self, driver, locatorName, locatorValue):
    ####locator="//*[@"+locatorName+"='"+locatorValue+"']"
    #####print locator
   ##### el = driver.find_element_by_xpath(locator)
   ##### print el
   ##### el.click()
    #####wait_for_page_load(self, 20)

#def wait_for_page_load(self, timeout=30):
    #old_page = self.find_element_by_tag_name('html')
   # yield
   # WebDriverWait(self, timeout).until(staleness_of(old_page))


# ----------------------------------------------------------------------

def safe_unicode(obj, *args):
    """ return the unicode representation of obj """
    try:
        return unicode(obj, *args)
    except UnicodeDecodeError:
        # obj is byte string
        ascii_text = str(obj).encode('string_escape')
        return unicode(ascii_text)

def safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('unicode_escape')

#getTestData(1)
#startId - first test case
#endId -last test case
#browserName - browser if empty default will be chrome
#testCaseFile - location of test cases if empty will use testcases.xlsx from local directory
#SheetName - name of spreadsheet, if empty will use Sheet1 as default value

#TestRunner (1, 1, "", "/Users/Lena/PycharmProjects/CMP_NEW/testcases.xlsx", "Sheet1")
#TestRunner (1, 1, "firefox", "/Users/Lena/PycharmProjects/testcases.xlsx", "Sheet1")


def TestRunner (startCase, endCase, browser, env, test_case_file, sheet_name):
    global startId
    global endId
    global browserName
    global testCaseFile
    global SheetName
    global Environment

    if browser!="":
        browserName = browser
    if startCase!="":
        startId=startCase
    if endCase!="":
        endId=endCase
    if browser!="":
        browserName=browser
    if env!="":
        Environment=env
    if test_case_file != "":
        testCaseFile = test_case_file
    if sheet_name != "":
        SheetName = sheet_name

    suite = unittest.TestSuite()
    ##Add additional test suites as classes here:
    suite.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(CMPsuite)
                ])

            # Invoke TestRunner
    dir = os.getcwd()
    report_file = open(dir+"TestExecutionReport.html", "w")
            #runner = unittest.TextTestRunner(buf)       #DEBUG: this is the unittest baseline
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=report_file,
        title='CMP Test Report',
        verbosity=0,
        description='CMP data-driven test suite execution on '+env+' environment'
    )
    runner.run(suite)

TestRunner (1, 6, "chrome", "Production", "/Users/Lena/PycharmProjects/CMP_NEW/testcases.xlsx", "Sheet1")
