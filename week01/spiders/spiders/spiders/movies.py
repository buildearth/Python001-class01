# -*- coding: utf-8 -*-
import scrapy
from spiders.items import SpidersItem
from bs4 import BeautifulSoup as bs
from scrapy.selector import Selector

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    # def parse(self, response):
    #     pass
    def start_requests(self):
        for i in range(0,10):
            alink = 'https://movie.douban.com/top250?start={}&filter='.format(i*25)
            yield scrapy.Request(url = alink, callback = self.parse)


    '''
        使用beautifulSoup选择数据
    '''
    # def parse(self, response):
    #     soup = bs(response.text, 'html.parser')
    #     titles = soup.find_all('div', {'class': 'hd'})
    #     # items = []
    #     for titl in titles:
    #         item = SpidersItem()
    #         movie_name = titl.find('a').find('span').text
    #         movie_link = titl.find('a').get('href')
    #         item['title'] = movie_name
    #         item['link'] = movie_link
    #         # items.append(item)
    #         yield scrapy.Request(url = movie_link, meta = {'item': item}, callback = self.parse_info)
    #     # print(items)
    #     # return items

    # def parse_info(self, response):
    #     item = response.meta['item']
    #     soup = bs(response.text, 'html.parser')
    #     show_data = soup.find('span', {'property':'v:initialReleaseDate'}).text
    #     score = soup.find('strong', {'class':'ll rating_num'}).text
    #     item['show_data'] = show_data
    #     item['score'] = score
    #     yield item

    '''
        使用scrapy的Selector选择数据
    '''
    def parse(self, response):
        movies = Selector(response = response).xpath('//div[@class="hd"]')
        for movie in movies:
            title = movie.xpath('./a/span/text()')
            href = movie.xpath('./a/@href')
            print('-'*20)
            # print(title)
            # print(href)
            # print('-'*20)
            print(title.extract_first().strip())
            print(href.extract_first().strip())

'''
有疑问到log
2020-06-23 23:13:06 [scrapy.core.downloader.tls] WARNING: Remote certificate is not valid for hostname "movie.douban.com"; '*.douban.com'!='movie.douban.com'
'''
