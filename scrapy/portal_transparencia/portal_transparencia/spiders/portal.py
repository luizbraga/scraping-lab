# -*- coding: utf-8 -*-
import scrapy


class PortalSpider(scrapy.Spider):
    name = 'portal'
    allowed_domains = ['http://www.portaltransparencia.gov.br/']
    start_urls = ['http://www.portaltransparencia.gov.br/']

    def __init__(self, *args, **kwargs):
        super(PortalSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        pass
