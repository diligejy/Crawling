# -*- coding: utf-8 -*-
import scrapy


class Class021Spider(scrapy.Spider):
    name = 'class02_1'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['http://blog.scrapinghub.com/']

    def parse(self, response):
        pass
