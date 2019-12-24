# -*- coding: utf-8 -*-
import scrapy

# 스파이더 종류 : CrawlSpider, XMLFeedSpider, CSVFeedSpider, SitemapSpider
class TestSpider(scrapy.Spider):
    name = 'test4'
    allowed_domains = ['blog.scrapinghub.com', 'daum.net', 'naver.com']
    
    # 실행 방법1
    # 멀티 도메인
    start_urls = ['http://blog.scrapinghub.com/', 'https://naver.com', 'https://daum.net']

    custom_settings = {
        'DOWNLOAD_DELAY' : 2
    }

    # 실행 방법2
    # Request 각각 지정
    # def start_request(self):
    #     yield scrapy.Request('http://blog.scrapinghub.com/', self.parse)
    #     yield scrapy.Request('http://blog.scrapinghub.com/', self.parse)
    #     yield scrapy.Request('http://blog.scrapinghub.com/', self.parse)


    # 분기 처리
    def parse(self, response):
        self.logger.info('Response URL : %s'% response.url)
        self.logger.info('Response Status : %s'% response.status)

        # print('type is : ', type(response.body))
        if response.url.find('scrapinghub'):
            yield {
                'sitemap' : response.url,
                'contents' : response.body[:100]
            }
        elif response.url.find('naver'):
            yield {
                'sitemap' : response.url, 
                'contents' : response.body[:100]
            }
        else:
            yield {
                'sitemap' : response.url,
                'contents' : response.body[:100],
                'title' : response.css('').getall()
            }


