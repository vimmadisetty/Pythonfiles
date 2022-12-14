
from wsgiref import headers
import requests
from urllib import response
import csv
from requests.api import head
import pandas as pd

#url='https://api.census.gov/data/2020/cbp?get=NAME,NAICS2017_LABEL,NAICS2017,ESTAB,PAYANN,PAYQTR1,EMP&for=county:*&YEAR=2020'
#url='https://api.census.gov/data/2020/cbp?get=NAME,NAICS2017_LABEL,ESTAB,PAYANN,PAYQTR1,EMP&for=county:*&YEAR=2020&NAICS2017=311&NAICS2017=312&NAICS2017=313&NAICS2017=314&NAICS2017=315&NAICS2017=316&NAICS2017=321&NAICS2017=322&NAICS2017=323&NAICS2017=324&NAICS2017=325&NAICS2017=326&NAICS2017=327&NAICS2017=331&NAICS2017=332&NAICS2017=333&NAICS2017=334&NAICS2017=335&NAICS2017=336&NAICS2017=337&NAICS2017=339'
#url='https://api.census.gov/data/2020/cbp?get=NAME,NAICS2017_LABEL,ESTAB,PAYANN,PAYQTR1,EMP&for=county:*&YEAR=2020&NAICS2017=3111&NAICS2017=3112&NAICS2017=3113&NAICS2017=3114&NAICS2017=3115&NAICS2017=3116&NAICS2017=3117&NAICS2017=3118&NAICS2017=3119&NAICS2017=3121&NAICS2017=3122&NAICS2017=3131&NAICS2017=3132&NAICS2017=3133&NAICS2017=3141&NAICS2017=3149&NAICS2017=3151&NAICS2017=3152&NAICS2017=3159&NAICS2017=3161&NAICS2017=3162&NAICS2017=3169&NAICS2017=3211&NAICS2017=3212&NAICS2017=3219&NAICS2017=3221&NAICS2017=3222&NAICS2017=3231&NAICS2017=3241&NAICS2017=3251&NAICS2017=3252&NAICS2017=3253&NAICS2017=3254&NAICS2017=3255&NAICS2017=3256&NAICS2017=3259&NAICS2017=3261&NAICS2017=3262&NAICS2017=3271&NAICS2017=3272&NAICS2017=3273&NAICS2017=3274&NAICS2017=3279&NAICS2017=3311&NAICS2017=3312&NAICS2017=3313&NAICS2017=3314&NAICS2017=3315&NAICS2017=3321&NAICS2017=3322&NAICS2017=3323&NAICS2017=3324&NAICS2017=3325&NAICS2017=3326&NAICS2017=3327&NAICS2017=3328&NAICS2017=3329&NAICS2017=3331&NAICS2017=3332&NAICS2017=3333&NAICS2017=3334&NAICS2017=3335&NAICS2017=3336&NAICS2017=3339&NAICS2017=3341&NAICS2017=3342&NAICS2017=3343&NAICS2017=3344&NAICS2017=3345&NAICS2017=3346&NAICS2017=3351&NAICS2017=3352&NAICS2017=3353&NAICS2017=3359&NAICS2017=3361&NAICS2017=3362&NAICS2017=3363&NAICS2017=3364&NAICS2017=3365&NAICS2017=3366&NAICS2017=3369&NAICS2017=3371&NAICS2017=3372&NAICS2017=3379&NAICS2017=3391&NAICS2017=3399'
url='https://api.census.gov/data/2010/cbp?get=CSA,EMP,EMP_F,EMP_N,EMP_N_F,EMPSZES,EMPSZES_TTL,ESTAB,ESTAB_F,FOOTID_GEO,FOOTID_NAICS,GEO_ID,GEO_TTL,GEOTYPE,LFO,LFO_TTL,MD,MSA,NAICS2007,NAICS2007_TTL,PAYANN,PAYANN_F,PAYANN_N,PAYANN_N_F,PAYQTR1,PAYQTR1_F,PAYQTR1_N,PAYQTR1_N_F,ST,YEAR&for=county:*&YEAR=2010'
headers={
    'Accept':'application/json',
    'Content-Type':'application/json'
}

response=requests.request("GET",url,headers=headers,data={})
myjson=response.json()
ourdata=[]
for x in myjson:
    listing=[x[:1],x[1:2],x[2:3],x[3:4],x[4:5],x[5:6],x[6:7],x[7:8],x[8:9],x[9:10],x[10:11],x[11:12],x[12:13],x[13:14],x[14:15]]
    ourdata.append(listing)

with open('CBP_4digit_Manufacturing_2020.csv', 'w',encoding='UTF8',newline='') as f:
    writer=csv.writer(f)
    writer.writerows(ourdata)

print('Done')