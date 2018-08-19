# -*- coding: utf-8 -*- 
import requests,time
import urlparse
from bs4 import BeautifulSoup
import csv

 

############################

f = open("oldstr.csv","ab" )        #後面參數不同效果不同
w = csv.writer(f, dialect='excel')   #dialect='excel'寫不同行

#標題
b=['古蹟名','照片網址','介紹','地址','經度','緯度']
c=[]
for i in range(0,6):
    c.append(b[i])  #.decode('utf8').encode('utf8')
#print type(c[0])
#print c
w.writerow(b)
f.close() 

rs=requests.session()

a1="http://www.boch.gov.tw/boch/frontsite/cultureassets/CultureAssetsTotalSearchAction.do?maxRecord=10&menuId=310&searchType=1.1%23%E5%8F%A4%E8%B9%9F&align=center&recordCount=802&iscancel=true&currentPage="
a2="&method=doSearchTotal&assetsName="
for i in range(1,82):
    res = rs.get(a1+str(i)+a2)
    #print res.encoding
    response = res.text.encode('utf8')
    soup = BeautifulSoup(response)
    #print soup
    rec_number = soup.find('table', {'title': '文化資產個案列表'}).findAll('td', {'class': 'forms_ItemLeft'})
    for rec_add in rec_number:        
        link_add =urlparse.urljoin("http://www.boch.gov.tw/boch/frontsite/cultureassets/",rec_add.find('a').get('href'))
        #print link_add
        #download(link_add)
        
        res = requests.get(link_add)
        response = res.text.encode('utf8')
        soup = BeautifulSoup(response)
        rec_number = soup.find('table', {'class': 'assets_detail'})
        #print soup
        rec_number_element=rec_number.findAll('tr')
#標題
        rec_number1 = soup.find('div',  {'style': 'padding-left: 55px'}).text   #.f('utf8')
        a=[rec_number1.encode('utf8')]   #encode成utf8 、cp950可以執行，印出未知碼，notepad++不能看。 不encode會有錯
        

        print a[0]
#圖片            
        f = open("oldstr.csv","ab+" )        #後面參數不同效果不同
        w = csv.writer(f, dialect='excel')   #dialect='excel'寫不同行
        
        
        rec_number2 = soup.find('td',  {'align': 'center'},{'valign': 'middle'} ).find('img').get('src')
        link_href =urlparse.urljoin("http://www.boch.gov.tw/boch/",rec_number2)
        #print link_href
        a.append(link_href.encode('utf8'))
        #w.writerow([link_href])
#其他
        for one in rec_number_element:
            if one.find('td') is not None:
                if one.find('td').find('span') is not None:
                    #print one.find('td').find('span').text
                    if (one.find('td').find('span').text==u'所在地理區域')|(one.find('td').find('span').text==u'地址或位置')|(one.find('td').find('span').text==u'歷史沿革')|(one.find('td').find('span').text==u'經度')|(one.find('td').find('span').text==u'緯度'):                
                        #print type(  ''.join(one.find('td', {'class': 'even'}).text.split()).encode('utf8')   )                
                        #w.writerow([ ''.join(one.find('td', {'class': 'even'}).text.split()).encode('cp950')  ])
                        a.append(''.join(one.find('td', {'class': 'even'}).text.split()).encode('utf8'))    #.encode('utf8')
        #print type(a[0])
        c=a[3]+','+a[4]
        #d=a[4]+','+a[5]
        b=(a[0],a[1],a[2],c,a[5],a[6])

        w.writerow(b)   #寫一行用此，寫多行用writerows
        f.close()
        time.sleep(3)   
        

