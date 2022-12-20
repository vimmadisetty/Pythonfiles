import requests
import urllib
from urllib import response
import csv
from requests.api import head



url='https://api.census.gov/data/2019/acs/acs5?get=NAME&for=tract:*&in=state:14'


status_code = urllib. request. urlopen(url). getcode()
print(status_code)
