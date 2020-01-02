from bs4 import BeautifulSoup
import requests

r=requests.get(
    "https://www.cwb.gov.tw/V7/forecast/f_index.htm?_=1575700472301",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
)

r.encoding="utf8"
# print(r.text)
w1 = BeautifulSoup(r.text, "html.parser")
country = w1.find_all("td",{"width":"60%"})
temperture = w1.find_all("td",{"width":"50%"})

z1 = 0
country_list =[]
for z1 in country:
    country_list.append(z1.text)
    # print(z1.text)
print(country_list)
temperture_list = []
for z2 in temperture:
    temperture_list.append(z2.text)
    # print(z2.text)
print(temperture_list)

import pandas as pd

t = pd.DataFrame({"縣市":country_list,"溫度":temperture_list})
print(t)



