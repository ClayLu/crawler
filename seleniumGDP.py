# -*- coding: utf-8 -*-
from selenium import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import urlparse
import csv

browser = webdriver.Firefox()
browser.get('http://statdb.dgbas.gov.tw/pxweb/Dialog/..%5CDialog%5Cvarval.asp?ma=NA8101A1A&ti=%B0%EA%A5%C1%A9%D2%B1o%B2%CE%ADp%B1%60%A5%CE%B8%EA%AE%C6%282008SNA%29-%A6~&path=../PXfile/NationalIncome/&lang=9&strList=L')
#browser.find_element_by_link_text("2005").click()
#browser.add_selection("name=values1", "label=2005")
select = Select(browser.find_element_by_name("values1"))
select.select_by_visible_text("2005")
select = Select(browser.find_element_by_name("values1"))
select.select_by_visible_text("2006")
select = Select(browser.find_element_by_name("values1"))
select.select_by_visible_text("2007")
select = Select(browser.find_element_by_name("values1"))
select.select_by_visible_text("2008")
select = Select(browser.find_element_by_name("values1"))
select.select_by_visible_text("2009")
select = Select(browser.find_element_by_name("values1"))
select.select_by_visible_text("2010")
select = Select(browser.find_element_by_name("values1"))
select.select_by_visible_text("2011")
select = Select(browser.find_element_by_name("values1"))
select.select_by_visible_text("2012")
select = Select(browser.find_element_by_name("values1"))
select.select_by_visible_text("2013")
select = Select(browser.find_element_by_name("values1"))
select.select_by_visible_text("2014")
select = Select(browser.find_element_by_name("values1"))
select.select_by_visible_text("2015")
select = Select(browser.find_element_by_name("values2"))
select.select_by_visible_text("國內生產毛額GDP(名目值，百萬元)")
select = Select(browser.find_element_by_name("values3"))
select.select_by_visible_text("原始值")

browser.find_element_by_name("sel").click()
soup = BeautifulSoup(browser.page_source, "lxml")
table = soup.find('table',  {'class': 'pxtable'} ).find('tbody')
rows = table.find_all('tr')

f = open("C:\Users\clay\Desktop\oldstr.csv","wb" )        
w = csv.writer(f , delimiter=' ',quotechar='|') 

for row in rows:
	if row.find('td' , {'class': 'stub1'}) :
		c = [td.text.strip()  for td in row.find_all('td')]
		b = (c[0] , c[1].replace(",","") )
		print  c

			
		w.writerow(b)


f.close()
browser.close()