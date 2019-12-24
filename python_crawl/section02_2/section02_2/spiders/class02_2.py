# -*- coding: utf-8 -*-
import scrapy


class Class022Spider(scrapy.Spider):
    name = 'test3'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['http://blog.scrapinghub.com/']

    def parse(self, response):
        """
        :param : response
        :return : Request
        """
        for url in response.css('div.post-item > div > a::attr("href")').getall():
            # url 바로 사용 하기보다 urljoin 사용
            # yield scrapy.Request(url)
            yield scrapy.Request(response.urljoin(url), self.parse_title)
    
    def parse_title(self, response):
        """
        상세 페이지 -> 타이틀 추출
        :param : response
        :return text
        """

        contents = response.css('div.post-body > span > p::text').extract()[:10] # getall() 가능

        # print(contents) 
        yield {'contents' : ''.join(contents)} # List를 Text로 변환 ''.join()