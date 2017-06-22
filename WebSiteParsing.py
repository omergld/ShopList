from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
class Search(object):
    url=""
    def __init__(self, url):
      self.url=url


    def searchProduct(self,name):
         driver.get(self.url+name)
         html=driver.find_elements_by_class_name("product-item")
         products={}
         for product in html:
             print product.find_element_by_class_name("name")








