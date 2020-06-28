# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title = scrapy.Field()
    link = scrapy.Field()
    show_data = scrapy.Field()
    score = scrapy.Field()

class MaoYanItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    show_time = scrapy.Field()
    movie_type = scrapy.Field()
