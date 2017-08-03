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

driver = "";


class scarpping(object):


    def waitforelement(self,findwhat,value):
        wait = WebDriverWait(driver, 60)
        if findwhat=="id":
            element = wait.until(EC._element_if_visible((By.ID, value)))
        if findwhat=="class":
            element = wait.until(EC._element_if_visible((By.CLASS_NAME, value)))
        if findwhat=="css":
            element = wait.until(EC._element_if_visible((By.CSS_SELECTOR, value)))



    def initbrowser(self):
        driver=webdriver.WebDriver("./chromedriver")
        driver.get("https://www.rami-levy.co.il/")
        driver.set_window_size(1500, 1500)
        self.waitforelement("id","shoping_start_but")
        driver.find_element_by_id("shoping_start_but").click()

    def getProductByName(self,name):
        products = {}
        self.waitforelement("id","strSearch")
        driver.find_element_by_class_name("strSearch").send_keys(name)
        driver.find_element_by_class_name("strSearch").submit()
        webproducts=driver.find_elements_by_class_name("product_item")
        print(webproducts)
        # for item in webproducts:
        # for item in webproducts:
        #     name = item.find_element_by_class_name("prod_title prodName").get_attribute("innerHTML");
        #     price = item.find_element_by_class_name("prodPrice").get_attribute("innerHTML");
        #     products[name] = price
        # return json.dumps(products)
