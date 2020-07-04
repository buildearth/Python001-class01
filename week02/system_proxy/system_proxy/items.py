# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SystemProxyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DouBanTopItem(scrapy.Item):
    top_type = scrapy.Field()
    name = scrapy.Field()  # 书名
    auth = scrapy.Field()  # 作者
    book_type = scrapy.Field()  # 类型
    update_status = scrapy.Field()  # 更新还是完结
    intro = scrapy.Field()  # 简介
