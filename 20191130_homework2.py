import requests
import codecs
r=requests.get(
	"http://teaching.bo-yuan.net/test/",
	headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
		"Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
		# "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
	},
	params={
		"Lang":"zh-tw"
	},
	data={
		"action":"requests"
	}
)
r.encoding="utf8"
print("1,get:",r.text)

r=requests.delete(
	"http://teaching.bo-yuan.net/test/",
	headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
		"Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
		# "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
	},
	params={
		"Lang":"zh-tw"
	},
	data={
		 "action":"requests"
	}
)
r.encoding="utf8"
print("2,delete:",r.text)

r=requests.put(
	"http://teaching.bo-yuan.net/test/",
	headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
		"Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
		# "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
	},
	params={
		"Lang":"zh-tw"
	},
	data={
		"action":"requests"
	}
)
r.encoding="utf8"
print("3,put:",r.text)

r=requests.patch(
	"http://teaching.bo-yuan.net/test/",
	headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
		"Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
		# "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
	},
	params={
		"Lang":"zh-tw"
	},
	data={
		"action":"requests"
	}
)
r.encoding="utf8"
print("4,patch:",r.text)

r=requests.post(
	"http://teaching.bo-yuan.net/test/",
	headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
		"Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
		# "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
	},
	params={
		"Lang":"zh-tw"
	},
	data={
		"action":"requests"
	}
)
r.encoding="utf8"
print("5,post:",r.text)

# r.encoding="utf8"
# print(r.encoding)
# for d in r.headers:
# 	print(d,r.headers[d])
# print(r.text)
f=codecs.open("2019-11-30.html","w","utf8")
f.write(r.text)
f.close()