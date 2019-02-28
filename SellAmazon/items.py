# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose,Compose,TakeFirst


class ProductItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(
        input_processor=MapCompose(str.strip)
    )
    last_updated=scrapy.Field()
