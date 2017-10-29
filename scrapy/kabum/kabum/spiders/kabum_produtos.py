# -*- coding: utf-8 -*-
import scrapy


class KabumProdutosSpider(scrapy.Spider):
    name = 'kabum-produtos'
    allowed_domains = ['https://www.kabum.com.br/']
    start_urls = ['http://https://www.kabum.com.br//']

    def parse(self, response):
        pass
