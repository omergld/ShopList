# -*- coding: utf-8 -*-
from automation import scarpping
scar=scarpping()
scarpping.initbrowser(scar)
list=scarpping.getProductByName(scar,"פריגת")
for product in list:
    print(product)
scarpping.closebrowser(scar)