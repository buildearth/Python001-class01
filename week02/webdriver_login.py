#webDriver模拟浏览器行为
'''
webdriver & chromedriver(放到虚拟环境venv下的bin目录中，与当前机器中浏览器版本保持一致)
ChromeDriver下载地址：https://chromedriver.storage.googleapis.com/index.html
'''
from selenium import webdriver
import time
email = input('输入邮箱帐号:').strip()
pwd = input('输入密码:').strip()

try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im/login?from=home')  # 拉起浏览器,进入到指定网页
    time.sleep(1)
    # 找到输入的文本框，send_keys发送要填写的数据
    browser.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys(email)
    browser.find_element_by_xpath('//input[@name="password"]').send_keys(pwd)
    time.sleep(3)
    login_btn = browser.find_element_by_xpath('//button[@class="sm-button submit sc-1n784rm-0 bcuuIb"]')
    login_btn.click()  # 模拟button点击
    time.sleep(5)
    print(browser.page_source)  # 拿到网页源代码后可以使用xpath拿到结构化的内容
    cookies = browser.get_cookies() # 获取cookies,不是永久有效，到一定时间会过期
    print(cookies)
    time.sleep(3)
except Exception as e:
    print(e)
finally:
    browser.close()


# #如果文件下载内容过于庞大，可以分块下载
# import requests
# file_url = ""
# r = requests.get(file_url, stream = True)
# with open('xx.pdf', mode = 'wb') as pdf:
#     for data in r.iter_content(chuck_size = 2000):
#         if data
#             pdf.write(data)
