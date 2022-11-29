import urllib
from wsgiref import headers
import requests
from urllib import response
import csv
from requests.api import head
import pandas as pd


count=0
i=1
data=[]

while i<=70:
    if i < 10:
        url1='https://api.census.gov/data/2020/acs/acs5?get=NAME&for=tract:*&in=state:0{}'
        formatting=url1.format(i)
        status_code = urllib. request. urlopen(formatting). getcode()
        if status_code==200:
            response=requests.get(formatting).json()
            for j in response:
                listing=[j[:1],j[1:2],j[2:3],j[3:4]]
                data.append(listing)
            count=count+1
    else:
        url1='https://api.census.gov/data/2020/acs/acs5?get=NAME&for=tract:*&in=state:{}'
        formatting=url1.format(i)
        status_code = urllib. request. urlopen(formatting). getcode()
        if status_code==200:
            response=requests.get(formatting).json()
            for j in response:
                listing=[j[:1],j[1:2],j[2:3],j[3:4]]
                data.append(listing)
            count=count+1

    i=i+1


with open('censustract_response_All_states_2020.csv', 'w',encoding='UTF8',newline='') as f:
    writer=csv.writer(f)
    writer.writerows(data)

df1=pd.read_csv('censustract_response_All_states_2020.csv')

df1=df1.replace("'",'',regex=True)
df1=df1.replace("\[",'',regex=True)
df1=df1.replace("\]",'',regex=True)

df1.to_csv('Cleaned_censustract_All_states_2020.csv',index=False)

print('Done')
print(count)




