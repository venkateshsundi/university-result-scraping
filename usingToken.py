# import libraries
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
import xlrd 
import xlsxwriter

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
with xlsxwriter.Workbook('result.xlsx') as workbook:
	worksheet = workbook.add_worksheet()
	for row_num, data in enumerate(marks):
		worksheet.write_row(row_num, 0, data)
