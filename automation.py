from selenium import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import json

driver = webdriver.WebDriver( "./chromedriver")

class automation:


    def initBrowser(self):

        driver.get("https://www.rami-levy.co.il/")
        driver.set_window_size(1500,2000)
        driver.find_element_by_class_name("shoping_start_but wcag-underline").click()

    def getProductByName(name):
        products={}
        driver.find_element_by_class_name("strSearch").send_keys(name)
        driver.find_element_by_class_name("strSearch").submit()
        for item in driver.find_element_by_class_name("product_item"):
            name=item.find_element_by_class_name("prod_title prodName").get_attribute("innerHTML");
            price=item.find_element_by_class_name("prodPrice").get_attribute("innerHTML");
            products[name]=price

        return json.dumps(products)






