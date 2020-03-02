from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = 'C:/Users/jinyoung/Pictures/Crawling/janjaemi/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get('https://python.org')
# title에 Python이 없으면 에러를 발생
assert "Python" in driver.title

# <input id="id-search-field" name="q">
# 태그 name으로 특정한 태그를 찾을 수 있음
# find_element_by_name('q')
# find_elements_by_name('')
elem = driver.find_element_by_name('q')

# clear() : input 텍스트 초기화 하기
# send_keys(키워드) : 키보드 입력값 전달하기
#    - Keys.RETURN - 엔터키
#    - dir(Keys)로 키에 대응되는 이름 찾기

# input 텍스트 초기화
elem.clear()

# 키 이벤트 전송
elem.send_keys('Python')

# 엔터 입력
elem.send_keys(Keys.RETURN)

# assert로 driver.page_source에서 특정 키워드 확인하기
# time.sleep()함수로 일정시간 브라우저 내용 확인할 수 있도록 하기
# driver.quit()함수로 브라우저 끝내기

assert "No results found." not in driver.page_source

# 명시적으로 일정 시간 기다리기
time.sleep(1)

h3s = driver.find_elements_by_tag_name("h3")
for h3 in h3s:
    print(h3.text)