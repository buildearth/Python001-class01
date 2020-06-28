# -*- coding: utf-8 -*-
import scrapy
from spiders.items import MaoYanItem
from bs4 import BeautifulSoup as bs
from scrapy.selector import Selector
'''
使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
'''
class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    # def parse(self, response):
    #     pass
    def start_requests(self):
        yield scrapy.Request(url = 'https://maoyan.com/board/4', callback=self.start_crawl)

    def start_crawl(self, response):
        for movie in Selector(response = response).xpath('//div[@class="movie-item-info"]'):
            item = MaoYanItem()
            title = movie.xpath('./p/a/@title').extract_first().strip()
            link = "https://maoyan.com{}".format(movie.xpath('./p/a/@href').extract_first().strip())
            print(title, link)
            item['title'] = title
            item['link'] = link
            yield scrapy.Request(url = link, meta = {'item':item}, callback=self.parse)

    def parse(self, response):
        item = response.meta['item']
        movie = Selector(response = response).xpath('//div[@class="movie-brief-container"]')
        show_type = movie.xpath('./ul/li/a/text()').extract()
        show_time = movie.xpath('./ul/li/text()').extract()[-1]
        item['show_time'] = show_time
        item['movie_type'] = ','.join(show_type)
        yield item
