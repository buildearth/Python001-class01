import requests
from fake_useragent import UserAgent
'''
作业：requests模拟登录石墨文档
遇到问题：
    模拟登录的时候返回403错误，是因为被反爬虫机制检测出来request headers中的值不全导致的
    要完全模拟浏览器的行为，就要和浏览器中的请求头保持一致，才能避免被检测出来是爬虫
'''
ua = UserAgent(verify_ssl = False)
headers = {
    'User-Agent': ua.random,
    'Referer': 'https://shimo.im/login?from=home',
    'x-requested-with': 'XmlHttpRequest'
}

usr_name = input('输入邮件帐号：').strip()
pwd = input('输入密码：').strip()
form_data = {
    'email': usr_name,
    'password': pwd
}

login_url = 'https://shimo.im/lizard-api/auth/password/login'
with requests.session() as s:
    s.post(login_url, data = form_data, headers = headers)
    print(s.cookies)
    res = s.get('https://shimo.im/inbox')
    print(res.text)



















res = requests.post(login_url, data= form_data, headers = headers)
print(res.cookies)
