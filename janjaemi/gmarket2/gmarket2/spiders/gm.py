# -*- coding: utf-8 -*-
import scrapy


class GmSpider(scrapy.Spider):
    name = 'gm'

    # start_url이 없어도 start_requests를 먼저 실행

    def start_requests(self):
        yield scrapy.Request(url="http://corners.gmarket.co.kr/Bestsellers", callback=self.parse_mainpages)
        yield scrapy.Request(url='http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G01', callback=self.parse_subcategories)

    def parse_mainpages(self, response):
        pass

    def parse_subcategories(self, response):
        pass