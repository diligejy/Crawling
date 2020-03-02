from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
