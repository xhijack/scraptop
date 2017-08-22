# -*- coding: utf-8 -*-
"""
created by xhijack@gmail.com
updated: August 5 2017
"""
from __future__ import unicode_literals
import scrapy
import json

from scrapy import Request

from scraptop.helpers import string2integer
from scraptop.items import Product

DOMAIN = 'ace.tokopedia.com'


class TokopediaSpider(scrapy.Spider):
    name = "shopee"
    allowed_domains = ["shopee.co.id"]
    # start_urls = [SEARCH_URL.format(domain=DOMAIN, shop_id=24, start=0)]

    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.start_urls =[
            # 'https://shopee.co.id/{shop_name}?tab=product'.format(shop_name=shop_name)
            'https://shopee.co.id/api/v1/search_items/?by=sales&order=desc&newest=0&limit=30&skip_price_adjust=false&page_type=shop&match_id=15221534'
        ]


    def parse(self, response):
        items = json.loads(response.body)['items']
        for item in items:
            url_string = "https://shopee.co.id/api/v1/item_detail/?item_id={item_id}&shop_id=15221534".\
                format(item_id=item['itemid'])
            yield Request(url_string, callback=self.parse_detail)

    def parse_detail(self, response):
        item = json.loads(response.body)
        import pdb
        pdb.set_trace()
