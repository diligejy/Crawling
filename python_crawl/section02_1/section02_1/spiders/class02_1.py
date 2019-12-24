# -*- coding: utf-8 -*-
import scrapy


class Class02_Spider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        """
        :param : response
        :return : Title Text
        """
        
        # 2가지 (CSS Selector, XPath)
        # get() <-> getall(), extract() <-> extract_first()

        # 예제1
        # for text in response.css('div.post-header h2 a::text').getall():
        # Return Type : Request, BaseItem, dictionary, None
            # yield {'text': text}

        # 예제2
        for i, text in enumerate(response.xpath('//div[@class="post-header"]/h2/a/text()').getall()):
            # Return Type : Request, BaseItem, dictionary, None
            yield {
                'number': i,
                'text': text
            }
