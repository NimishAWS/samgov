from __future__ import print_function
from array import array
from cgitb import text
from itertools import dropwhile
from lib2to3.pgen2.driver import Driver
from multiprocessing import Value
from pkgutil import extend_path
from posixpath import split
from pydoc import describe
import re
from crypt import methods
from tabnanny import check
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import numpy as np
import pandas as pd
import csv  
import os

options = Options()
options.headless = True
driver = webdriver.Chrome()
driver.get('https://sam.gov/opp/38a110ac2ac04f50aaa5bec4f97e8d49/view')
driver.implicitly_wait(1)
content = driver.page_source

#for getting Notice ID
attachment = []


lik  = driver.find_element(By.ID, 'attachments-links')
print("SDASD")
l = driver.find_elements(By.XPATH,'//*[@id="opp-view-attachments-tableId"]/thead/th[1]')
print(l)
a= l.__getattribute__('th')
print(a)
k = lik.find_elements(By.CLASS_NAME, 'p_T-1x p_B-1x p_L-4x upload-table-doc-col ng-star-inserted')
print(k)
for i in k:
    print(i.get_attribute('href'))

#     # k = lik.find_elements(By.CSS_SELECTOR, '#opp-view-attachments-accordion-section > opp-sam-upload-v2 > div')
#     k = lik.find_elements(By.CSS_SELECTOR, 'a.opp-view-attachments-fileLinkId0 [href]')
#     print(k, 'kdasd')
#     i = k.__getattribute__('href')
#     print(i)

# for a in lik.find_elements(By.CSS_SELECTOR, 'a.opp-view-attachments-fileLinkId0[href]'):
    # print(a)

# except:
#     attachment.append("Null")

# print(attachment)