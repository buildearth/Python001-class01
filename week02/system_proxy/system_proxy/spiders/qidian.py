# -*- coding: utf-8 -*-
'''
作业一：
为 Scrapy 增加代理 IP 功能。
将保存至 csv 文件的功能修改为保持到 MySQL，并在下载部分增加异常捕获和处理机制。
备注：代理 IP 可以使用 GitHub 提供的免费 IP 库 https://www.zdaye.com/shanxi2_ip.html
'''
import scrapy
import os
from fake_useragent import UserAgent
from scrapy.selector import Selector
from system_proxy.items import DouBanTopItem

# os.environ['http_proxy'] = 'http://112.64.233.130:9991'
# os.environ['https_proxy'] = 'https://171.220.170.147:4514'
class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['qidian.com', 'httpbin']
    start_urls = ['https://qidian.com/']
    # start_urls = ['http://httpbin.org/ip']
    ua = UserAgent(verify_ssl = False)

    # def parse(self, response):
    #     print(response.text)
    def start_requests(self):
        self.headers = {
            'User-Agent': self.ua.random,
            'Referer': 'https://www.qidian.com/'
        }
        url = 'https://www.qidian.com/rank'
        yield scrapy.Request(url, headers = self.headers, callback = self.parse_top_link)

    def parse_top_link(self, response):
        top_selc = Selector(response = response).xpath('//div[@class="rank-list sort-list"]')
        top_type = top_selc.xpath('./h3[@class="wrap-title lang"]/text()').extract_first()
        top_link = 'http:%s'%top_selc.xpath('./h3/a/@href').extract_first()
        print(top_type, top_link)
        item = DouBanTopItem()
        item['top_type'] = top_type
        yield scrapy.Request(top_link, headers = self.headers, meta = {'item':item},\
            callback = self.handle_top_info)

    def handle_top_info(self, response):
        item = response.meta['item']
        for book in Selector(response = response).xpath('//div[@class="book-mid-info"]'):
            name = book.xpath('./h4/a/text()').extract_first().strip()
            auth, book_type, _ = book.xpath('./p/a/text()').extract()
            update_status = book.xpath('./p[@class="author"]/span/text()').extract_first()
            intro = book.xpath('./p[@class="intro"]/text()').extract_first().strip()
            item['name'] = name
            item['auth'] = auth
            item['book_type'] = book_type
            item['update_status'] = update_status
            item['intro'] = intro
            yield item
