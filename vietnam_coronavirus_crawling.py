#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

from selenium.webdriver.chrome.options import Options
opts = Options()
opts.add_argument("user-agent=manhdd")


# In[4]:


# create a new Chrome session
driver = webdriver.Chrome("/Users/manhdd/Downloads/chromedriver_2",options=opts)


# In[7]:


#Get the soup
url = "https://ncov.moh.gov.vn/"
driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content)


# In[31]:


#Navigate the two tables
table=soup.find_all(id='sailorTable',attrs={'class':"table table-striped table-covid19"})


# In[48]:


tinh_thanh_pho=[]
so_ca_nhiem=[]
dang_dieu_tri=[]
khoi=[]
tu_vong=[]
data_1=table[0].find('tbody') #this is table 1

#Navigate the data from table 1 and fit them to the lists above
for row in data_1.find_all('tr'):
    tinh_thanh_pho.append(row.find_all('td')[0].string)
    so_ca_nhiem.append(row.find_all('td')[1].string)
    dang_dieu_tri.append(row.find_all('td')[2].string)
    khoi.append(row.find_all('td')[3].string)
    tu_vong.append(row.find_all('td')[4].string)
    


# In[53]:


#Create a pd dataframe for table 1
df_1=pd.DataFrame({'Tỉnh/Thành phố':tinh_thanh_pho,'Số ca nhiễm':so_ca_nhiem,'Đang điều trị':dang_dieu_tri,'Khỏi':khoi,'Tử vong':tu_vong})


# In[63]:


#Extract the data to a csv file
df_1.to_csv('So_lieu_theo_tinh_thanh.csv',encoding="utf-8")


# In[51]:


benh_nhan=[]
tuoi=[]
gioi_tinh=[]
dia_diem=[]
tinh_trang=[]
quoc_tich=[]
data_2=table[1].find('tbody') #this is table 2

#Navigate the data from table 2 and fit them to the lists above
for row in data_2.find_all('tr'):
    benh_nhan.append(row.find_all('td')[0].string)
    tuoi.append(row.find_all('td')[1].string)
    gioi_tinh.append(row.find_all('td')[2].string)
    dia_diem.append(row.find_all('td')[3].string)
    tinh_trang.append(row.find_all('td')[4].string)
    quoc_tich.append(row.find_all('td')[5].string)


# In[58]:


#Create a pd dataframe for table 1
df_2=pd.DataFrame({'Bệnh nhân':benh_nhan,'Tuổi':tuoi,'Giới tính':gioi_tinh,'Địa điểm':dia_diem,'Tình trạng':tinh_trang,'Quốc tịch':quoc_tich})


# In[64]:


#Extract the data to a csv file
df_2.to_csv('So_lieu_theo_tung_ca_nhiem.csv',encoding="utf-8")


# In[ ]:




