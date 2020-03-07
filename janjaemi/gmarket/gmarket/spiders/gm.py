# -*- coding: utf-8 -*-
import scrapy


class GmSpider(scrapy.Spider):
    name = 'gm'
    allowed_domains = ['www.gmarket.co.kr/']
    start_urls = ['https://www.gmarket.co.kr//']

    def parse(self, response):
        pass
