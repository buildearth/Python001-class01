#webDriver模拟浏览器行为
'''
webdriver & chromedriver(放到虚拟环境venv下的bin目录中，与当前机器中浏览器版本保持一致)
ChromeDriver下载地址：https://chromedriver.storage.googleapis.com/index.html
'''
from selenium import webdriver
import time
#使用webdriver模拟登录豆瓣电影，获取到cookies,requests和BeatifulSoup解析
#思考：webdriver和scrapy结合使用，在scrapy什么位置调用？拿到的cookie如何使用？
#       scrapy有一个start_url,是最开始调用的start_request()可以在这个中实现，随机代理ip放到下载中间件，
try:
    browser = webdriver.Chrome()
    browser.get('https://accounts.douban.com')  # 拉起网页
    time.sleep(3)
    # print(browser.page_source)

    switch_frame_btn = browser.find_element_by_xpath('//div[@class="account-body-tabs"]')
    switch_frame_btn.click()
    print(switch_frame_btn.text)

    browser.find_element_by_xpath('//input[@id="username"]').send_keys('')
    browser.find_element_by_xpath('//input[@id="password"]').send_keys('')
except Exception as e:
    print(e)
finally:
    time.sleep(2)
    browser.close()
