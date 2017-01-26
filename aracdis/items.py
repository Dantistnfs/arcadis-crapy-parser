# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AracdisItem(scrapy.Item):
    # define the fields for your item here like:
    value = scrapy.Field()
    graph_type = scrapy.Field()
    value_name = scrapy.Field()
    city_name = scrapy.Field()
    city_region = scrapy.Field()
    pass
