# -*- coding: utf-8 -*-
import scrapy
import json
from naver_api.items import NaverApiItem

class NaSpider(scrapy.Spider):
    name = 'na'

    def start_requests(self):
        start_urls = 'https://openapi.naver.com/v1/search/shop.json?query='
        client_id = '7MHolTcJz4biLeHVU5Ia'
        client_secret = 'eQrRw9sLBY'
        header_params = {'X-Naver-Client-Id' : client_id, 'X-Naver-Client-Secret' : client_secret}
        query = 'iphone'
        yield scrapy.Request(url = start_urls + query, headers=header_params)

    def parse(self, response):
        data = json.loads(response.body_as_unicode())
        for item in data['items']:
            doc = NaverApiItem()
            doc['title'] = item['title']
            doc['link'] = item['link']
            doc['image'] = item['image']
            doc['lprice'] = item['lprice']
            doc['hprice'] = item['hprice']
            doc['mallName'] = item['mallName']
            doc['productId'] = item['productId']
            doc['productType'] = item['productType']
            yield doc

