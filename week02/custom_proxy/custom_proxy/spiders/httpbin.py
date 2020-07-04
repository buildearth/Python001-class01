# -*- coding: utf-8 -*-
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        print(response.text)
