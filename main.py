# from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import defer
from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess

from scraptop.spiders.tokopedia import TokopediaSpider


def main(filename='result.json', format='json', shop_id=None, by=None, category_id=None):
    # configure_logging()
    setting = get_project_settings()

    setting.update(
        {
            'FEED_FORMAT': format,
            'FEED_URI': filename
        }
    )

    runner = CrawlerProcess(setting)

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(TokopediaSpider,shop_id=shop_id, by="brand")
        reactor.stop()

    crawl()
    reactor.run()


if __name__ == '__main__':
    main()