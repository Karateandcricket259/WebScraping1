from bs4 import BeautifulSoup
import csv
import time
import requests
import pandas as pd
url='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")
startable=soup.find('table')
temp_list=[]
table_rows=startable.find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip()for i in td]
    temp_list.append(row)
starname=[]
radius=[]
mass=[]
distance=[]
luminosity=[]
for i in range(1,len(temp_list)):
    starname.append(temp_list[i][1])
    radius.append(temp_list[i][6])
    mass.append(temp_list[i][5])
    distance.append(temp_list[i][3])
    luminosity.append(temp_list[i][7])
dataframe=pd.DataFrame(list(zip(starname,radius,mass,distance,luminosity)),columns=['Proper name','Radius','Mass','Distance','Luminosity'])
print(dataframe)
dataframe.to_csv('star.csv')
