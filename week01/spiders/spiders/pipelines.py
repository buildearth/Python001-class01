# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd

class SpidersPipeline:
    def process_item(self, item, spider):
        data = [(item['title'], item['movie_type'], item['show_time'])]
        movies = pd.DataFrame(data = data)
        movies.to_csv('maoyan_top10_scrapy.csv', mode = 'at', encoding = 'utf-8',
            index = False, header = False)
        print('-'*10, data)
        return item
