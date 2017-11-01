# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver


class PortalSpider(scrapy.Spider):
    name = 'portal'
    allowed_domains = ['http://www.portaltransparencia.gov.br/']
    start_urls = ['http://www.portaltransparencia.gov.br/']

    def __init__(self, *args, **kwargs):
        super(PortalSpider, self).__init__(*args, **kwargs)
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(800, 600)

    def parse(self, response):
        pass
