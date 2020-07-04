#cookie的解决
#使用post方法，提交登录信息后，服务器会返回加密的用户名密码，即cookie.
import requests
from fake_useragent import UserAgent
ua = UserAgent(verify_ssl = False)
headers = {
    'User-Agent': ua.random,
    'Referer': 'https://accounts.douban.com/passport/login?source=movie'}
# r = requests.post('http://httpbin.org/post', headers = headers, data = {'key':'value'})
# print(r.json())

login_url = 'https://accounts.douban.com/j/mobile/login/basic'
form_data = {
    'ck': '',
    'name': '1234',
    'password': 'qwee',
    'remember': 'false',
    'ticket': ''
}
with requests.session() as s:
    r = requests.post(login_url, data = form_data, headers = headers)
    print(r.json())
