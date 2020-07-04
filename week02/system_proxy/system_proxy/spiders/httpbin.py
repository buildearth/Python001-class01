# -*- coding: utf-8 -*-
import scrapy
import os

os.environ['http_proxy'] = 'http://52.179.231.206:80'

class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        print(response.text)
