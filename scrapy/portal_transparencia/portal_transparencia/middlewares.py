# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse
from scrapy.utils.python import to_bytes


class SeleniumSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    def process_request(self, request, spider):
        request.meta['driver'] = self.driver
        self.driver.get(request.url)
        body = to_bytes(self.driver.page_source)

        return HtmlResponse(
            url=self.driver.current_url,
            body=body,
            encoding='utf-8',
            request=request
        )

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(800, 600)

    def spider_closed(self, spider):
        self.browser.close()
