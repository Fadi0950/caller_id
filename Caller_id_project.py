#prerequities
import requests
import pandas as pd
from bs4 import BeautifulSoup

def getdata(url):
    data=requests.get(url)
    print(data.json())
    return data.text


api='15b692b73449d3d65cca69444ffb9523'
number='9175467877'
country='IN'


html_data=getdata(
    'http://apilayer.net/api/validate?access_key='+api+'&number='+number+'&country_code='+country+'&format=1')

soup=BeautifulSoup(html_data,'html.parser')
print(soup)