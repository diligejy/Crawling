# Crawling
크롤링 전용


## KDKC

사용법 
1. pip install scrapy
2. pip install scrapy-fake-useragent

3-1. kdkc 폴더에서 명령어창을 오픈한 뒤 scrapy crawl kk -o 파일명.확장자(json, csv, pkl)을 입력

3-2. 혹은 kdkc폴더 안에 있는 spiders폴더 안에 다른 파이썬 스크립트를 생성한 뒤 
     os.system('scrapy crawl kk -o 파일명.확장자')를 입력하고 
     with open으로 불러와서 
