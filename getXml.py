from selenium import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.WebDriver( "./chromedriver")

class getmarket:
    @staticmethod
    def getxml():
        driver.get("http://prices.shufersal.co.il/")
        driver.find_element_by_id("ddlCategory").click()
        driver.find_element_by_css_selector("#ddlCategory > option:nth-child(3)").click()
        driver.find_element_by_css_selector("#gridContainer > table > tbody > tr:nth-child(1) > td:nth-child(1) > a").click()
        driver.get("chrome://downloads")
        file=driver.find_element_by_css_selector("#file-link").get_attribute("class")
        print "/users/omergoldstein/downloads/"+file

