# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyanimelistItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pic_urls = scrapy.Field()
    pass
