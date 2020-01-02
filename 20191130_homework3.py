import requests
import json
import prettytable

q= input("關鍵字:")
page = 1
while True:
	r=requests.get(
		"https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=" + str(q) + "&page=" + str(page) + "&sort=sale/dc",
		headers={
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
			"Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
			"Accept":"application/json, text/javascript, */*; q=0.01"
		},
		params={},
		data={}
	)

	# bi5 中文編碼 或者 utf8 萬國編碼
	r.encoding="utf8"

	# print(r.text)

	ret=json.loads(r.text)
	# 需自行用firefox查找pchome網頁,並用檢測元素,查找網路,XHR內的傳送資料

	t=prettytable.PrettyTable(["名稱","價格"], encoding="utf8")
	for d in ret["prods"]:
		t.add_row([d["name"],d["price"]])
	print(t)

	page = input("前往頁碼:")

