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

driver = webdriver.WebDriver("./chromedriver")


class scarpping(object):


    def waitforelement(self,findwhat,value):
        wait = WebDriverWait(driver, 120)
        if findwhat=="id":
            lookfor=driver.find_element_by_id(str(value))
            element = wait.until(EC.visibility_of(lookfor))
        if findwhat=="class":
            lookfor = driver.find_element_by_class_name(str(value))
            element = wait.until(EC.visibility_of(lookfor))
        if findwhat=="css":
            lookfor = driver.find_element_by_css_selector(By.CSS_SELECTOR, str(value))
            element = wait.until(EC.visibility_of(lookfor))



    def initbrowser(self):

        driver.get("https://www.rami-levy.co.il/")
        driver.maximize_window()
        self.waitforelement("class","shoping_start_but")
        driver.find_element_by_class_name("shoping_start_but").click()
        return "Browser is ready"

    def getProductByName(self,name):
        products = []
        self.waitforelement("id","strSearch")
        driver.find_element_by_id("strSearch").clear()
        driver.find_element_by_id("strSearch").send_keys(name)
        driver.find_element_by_id("strSearch").submit()
        webproducts=driver.find_elements_by_class_name("product_item")
        for item in webproducts:
            name = item.find_element_by_class_name("prodName").get_attribute("innerHTML");
            products.append(str(name.encode("utf-8")))
        return json.dumps(products)

    def closebrowser(self):
        driver.close()