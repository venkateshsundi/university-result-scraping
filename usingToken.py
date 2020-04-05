from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
path = 'chromedriver'
driver = webdriver.Chrome(path)
marks =[]
url = "https://jntuaresults.ac.in/view-results-56736237.html"
driver.get(url)
htnumber = driver.find_element_by_id('ht').send_keys('17jn1a0401')
search = driver.find_element_by_class_name('ci').click()

htno = "17jn1a0"
token = input('enter: ')
for i in range(401,460):
    url = "https://jntuaresults.ac.in/results/res.php?ht="+htno+str(i)+"&id=56736237&accessToken="+token
    driver.get(url)
    mark = driver.find_element(by=By.XPATH, value= '/html/body').text
    marks.append([int(s) for s in mark.split() if s.isdigit()])
