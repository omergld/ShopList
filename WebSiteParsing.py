from selenium import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.WebDriver( "./chromedriver",0,options)
class Search:
    def __init__(self, url):
      self.url=url


    def searchProduct(self,name):
         driver.get(self.url+name)
         html=driver.find_elements_by_class_name("product-item")
         products={}
         i=1
         for product in html:
             name= product.find_element_by_class_name("name").get_attribute("innerHTML")
             baseprice= product.find_element_by_css_selector("body > section > section > div > div > sp-items > div.items-wrapper > div.items > div:nth-child("+str(i)+") > div > sp-product > div.right.sp-product-price > span").get_attribute("innerHTML")
             price=baseprice[1:len(baseprice)]
             print name
             print price
             i=i+1

         driver.quit()









