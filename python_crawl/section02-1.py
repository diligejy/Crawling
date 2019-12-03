# Section 02-1
# 파이썬 크롤링 기초
# urllib 사용법 및 기본 스크래핑

import urllib.request as req

# 파일 URL
img_url = 'https://img1.daumcdn.net/thumb/R430x0.q70/?fname=https://t1.daumcdn.net/news/201808/13/iMBC/20180813162306998klwc.jpg'
html_url = 'https://google.com'

# 다운받을 경로
save_path1 = 'C:/python_crawl/test1.jpg'
save_path2 = 'C:/python_crawl/index.html'

# 예외 처리
try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('Download Failed')
    print(e)
else :  
    # Header 정보 출력
    print(header1)
    print(header2)

    # 다운로드 파일 정보
    print("Filename1 {}".format(file1))
    print("Filename2 {}".format(file2))
    print()

    # 성공
    print('Download Succeed')