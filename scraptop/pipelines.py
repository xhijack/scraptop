# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from __future__ import unicode_literals

import json
from copy import deepcopy
from sqlalchemy.exc import IntegrityError

from scraptop.database import db_session
from scraptop.models import db_connect, ProductTokopedia



class ScraptopPipeline(object):

    def __init__(self):
        self.Session = db_session

    def process_item(self, item, spider):
        session = self.Session()
        data = deepcopy(item)
        del data['image_urls']
        data['images'] = json.dumps(data['images'])
        product = ProductTokopedia(**data)
        # import pdb
        # pdb.set_trace()
        try:
            session.add(product)
            session.commit()

        except IntegrityError:
            print("Produk ID sudah ada")

        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
