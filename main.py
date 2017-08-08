# from scrapy.utils.log import configure_logging
import os
# from scrapy.utils.project import get_project_settings
# import settings as setting
from twisted.internet import defer
from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess

from scraptop.spiders.tokopedia import TokopediaSpider

# from scrapy.settings import Settings

# setting = Settings()
#
# setting_module_path = os.environ.get('SCRAPY_ENV', 'scraptop.settings')
# setting.setmodule(setting_module_path, priority='scraptop')
# print(setting.get('BASE_URL'))
import logging
from scrapy.utils.log import configure_logging

configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    filemode = 'a',
    format='%(levelname)s: %(message)s',
    level=logging.INFO
)

def main(filename='result.json', format='json', id_=None, by=None):
    # configure_logging()
    # setting = get_project_settings()
    setting = {}

    setting.update(
        {
            'FEED_FORMAT': format,
            'FEED_URI': filename,
            'IMAGES_STORE': 'tmp/images/',
            'USER_AGENT':  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'ITEM_PIPELINES': {
              'scrapy.pipelines.images.ImagesPipeline': 1
            },
            'BOT_NAME': 'scraptop',
            'SPIDER_MODULES': ['scraptop.spiders'],
            'NEWSPIDER_MODULE': 'scraptop.spiders',
        }
    )

    runner = CrawlerProcess(setting)

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(TokopediaSpider,id_=id_, by=by)
        reactor.stop()

    crawl()
    reactor.run()

import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Scrape Tokopedia.')
    parser.add_argument('--by', help='brand | category')
    parser.add_argument('--id', help='according ID id of SHOP or category')


    args = parser.parse_args()

    if args.by == 'brand':
        main(id_=args.id, by='brand')
    elif args.by == 'category':
        main(id_=args.id, by='category')
    else:
        logging.info("Please input parameter")
