# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from __future__ import unicode_literals

from scrapy import Item, Field


class Product(Item):
    product_id = Field()
    title = Field()
    weight = Field()
    categories = Field()
    price = Field()
    seller = Field()
    link_url = Field()
    location = Field()
    image_urls = Field()
    images = Field()
