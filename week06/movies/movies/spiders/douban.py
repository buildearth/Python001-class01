# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver

from movies.items import MoviesItem
class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    # def parse(self, response):
    #     pass
    def start_requests(self):
        link = 'https://movie.douban.com/subject/1292052/comments?status=P'
        yield scrapy.Request(url = link, callback = self.parse_get_short)


    def parse_get_short(self, response):
        movies = Selector(response = response).xpath('//div[@class="comment-item"]')
        for short in movies.xpath('//div[@class="comment-item"]'):
            text = short.xpath('./div/p/span/text()')
            star = short.xpath('./div/h3/span[@class="comment-info"]/span[@class="allstar50 rating"]/@title')
            item = MoviesItem()
            item['short'] = text.extract_first()
            item['star'] = star.extract_first()
            yield item

