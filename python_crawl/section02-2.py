# Section02-2
# 파이썬 크롤링 기초
# urlopen 함수 기초 사용법

import urllib.request as req
from urllib.error import URLError, HTTPError

# 다운로드 경로 및 파일명

path_list = ['C:/python_crawl/test1.jpg', 'C:/python_crawl/index.html']

# 다운로드 리소스 url
target_url = ['http://img.khan.co.kr/news/2019/01/01/l_2019010101000042400272942.jpg', \
'https://google.com']

for i, url in enumerate(target_url):
    # 예외 처리
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url)

        # 수신 내용
        contents = response.read()

        print("-----------------------------------------")

        # 상태 정보 중간 출력
        print('Header Info-{} : {}'.format(i, response.info()))
        print('HTTP Status Code : {}'.format(response.getcode()))
        print()
        print('---------------------------')
        
    except HTTPError as e:
        print('Download Failed')
        print('HTTPError Code :', e.code)
    except URLError as e:
        print('Download failed')
        print('URLError Reason : ', e.reason)
    # 성공
    else:
        print()
        print('Download Succeed')



