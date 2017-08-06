# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from scraptop.models import db_connect, create_tokopedia_table, ProductTokopedia

class ImagePipeline(object):
    # def __init__(self):

    def process_item(self, item, spider):
        return item
# class ScraptopPipeline(object):
#
#     def __init__(self):
#         import pdb
#         pdb.set_trace()
#         engine = db_connect()
#
#         create_tokopedia_table(engine)
#         self.Session = sessionmaker(bind=engine)
#
#     def process_item(self, item, spider):
#         session = self.Session()
#         product = ProductTokopedia(**item)
#
#         try:
#             session.add(product)
#             session.commit()
#
#         except IntegrityError:
#             print "Produk ID sudah ada"
#
#         except:
#             session.rollback()
#             raise
#         finally:
#             session.close()
#
#         return item
