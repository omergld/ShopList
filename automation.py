# -*- coding: utf-8 -*-
from selenium import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import json

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.WebDriver( "./chromedriver")

class automation(object):


    def __init__(self):
        pass



    @classmethod
    def waitForElement(classId):
        wait = WebDriverWait(driver, 60)
        element = wait.until(EC.element_to_be_clickable((By.ID,classId)))

    @classmethod
    def initBrowser(self):

        driver.get("https://www.rami-levy.co.il/")
        driver.set_window_size(1500,1500)
        self.waitForElement("shoping_start_but")
        driver.find_element_by_class_name("shoping_start_but").click()

    @classmethod
    def getProductByName(self,name):

        products={}
        self.waitForElement("strSearch")
        driver.find_element_by_class_name("strSearch").send_keys(name)
        driver.find_element_by_class_name("strSearch").submit()
        for item in driver.find_element_by_class_name("product_item"):
            name=item.find_element_by_class_name("prod_title prodName").get_attribute("innerHTML");
            price=item.find_element_by_class_name("prodPrice").get_attribute("innerHTML");
            products[name]=price
        return json.dumps(products)






