# -*- coding: utf-8 -*-
"""
created by xhijack@gmail.com
updated: August 5 2017
"""

import scrapy
import json

from scrapy import Request

from scraptop.helpers import string2integer
from scraptop.items import Product

DOMAIN = 'ace.tokopedia.com'
SEARCH_URL = 'https://{domain}/search/v2.6/product?shop_id={shop_id}&ob=11&rows=20&start={start}&' \
             'full_domain=www.tokopedia.com&scheme=https&device=desktop&source=shop_product'

CATEGORY_URL = 'https://ace.tokopedia.com/search/product/v3?full_domain=www.tokopedia.com&' \
               'scheme=https&device=desktop&source=directory&page=1&image_size=200&rows=75&sc={sc}' \
               '&start={start}&ob=23'

class TokopediaSpider(scrapy.Spider):
    name = "jakartanotebook"
    allowed_domains = ["jakartanotebook.com"]
    # start_urls = [SEARCH_URL.format(domain=DOMAIN, shop_id=24, start=0)]
    start_urls = ('https://www.jakartanotebook.com/notebook',)
    def __init__(self, shop_id=None, by=None, category_id=None):
        self.start_urls = ('https://www.jakartanotebook.com/notebook',)

    #     self.by = by
    #     self.category_id = category_id
    #     self.shop_id = shop_id
    #
    #     if self.by == 'brand':
    #         self.start_urls = (SEARCH_URL.format(domain=DOMAIN, shop_id=shop_id, start=0),)
    #     elif self.by == 'category':
    #         self.start_urls = (CATEGORY_URL.format(sc=self.category_id, start=0),)

    def parse(self, response):
        import pdb
        pdb.set_trace()
        # if self.by == 'brand':
        #     return self.parse_by_brand(response=response)
        # elif self.by == 'category':
        #     return self.parse_by_categories(response=response)

