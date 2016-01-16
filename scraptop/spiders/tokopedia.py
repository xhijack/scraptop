# -*- coding: utf-8 -*-
import scrapy
import json
from scraptop.items import Product

DOMAIN = 'ace.tokopedia.com'
SEARCH_URL = 'https://{domain}/search/v1/product?sq={keyword}&sc=1&rows=30&start=0&terms=true&ob=1'\
    .format(domain=DOMAIN, keyword='')


class TokopediaSpider(scrapy.Spider):
    name = "tokopedia"
    allowed_domains = ["tokopedia.com"]
    start_urls = (
        SEARCH_URL,
    )

    def __init__(self, keyword):
        self.keyword = keyword
        self.start_urls = (SEARCH_URL.format(keyword=keyword),)

    def parse(self, response):

        items = json.loads(response.body)
        products = []

        for item in items['data']:
            product = Product()
            product['product_id'] = item['id']
            product['title'] = item['name']
            product['price'] = item['wholesale_price'][0]['price']
            product['seller'] = item['shop']['name']
            product['link_url'] = item['uri']
            product['location'] = item['shop']['location']
            product['image_url'] = item['image_uri']
            products.append(product)

        return products
