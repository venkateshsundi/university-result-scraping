# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:23:48 2020

@author: venkatesh
"""

# import libraries
import pandas as pd
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
import xlrd 
import xlsxwriter
import pandas as pd

#initialization
path = 'chromedriver'
driver = webdriver.Chrome(path)
marks =[]
url = "https://jntuaresults.ac.in/view-results-56736237.html"
driver.get(url)
htnumber = driver.find_element_by_id('ht').send_keys('17jn1a0401')
search = driver.find_element_by_class_name('ci').click()



# input hall ticket worksheet  
loc = ("E:\python\htNumbers.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
 
# fetch result:scraper  
token = input('enter: ')
for i in range(sheet.nrows):
    url = "https://jntuaresults.ac.in/results/res.php?ht="+str(sheet.cell_value(i, 0))+"&id=56736237&accessToken="+token
    driver.get(url)
    mark = driver.find_element(by=By.XPATH, value= '/html/body').text
    marks.append([int(s) for s in mark.split() if s.isdigit()])

# write result into worksheet
df = pd.DataFrame(marks)
df = df.drop([3,7,11,15,19,23,27,31,32,33,34,35], axis = 1)
df['percentage'] = df.apply(lambda x: ((x[2] + x[6] + x[10] + x[14] + x[18] + x[22] + x[26] + x[30])/800)*100, axis=1)
df.to_excel("resultWithInternalExternal.xlsx")


df1 = pd.DataFrame(marks)
df1 = df1.drop([0,1,3,4,5,7,8,9,11,12,13,15,16,17,19,20,21,23,24,25,27,28,29,31,32,33,34,35], axis = 1)
df1['percentage'] = df1.apply(lambda x: ((x[2] + x[6] + x[10] + x[14] + x[18] + x[22] + x[26] + x[30])/800)*100, axis=1)
df1.to_excel("resultWithTotalOnly.xlsx")

