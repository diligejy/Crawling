from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = 'C:/Users/jinyoung/Pictures/Crawling/janjaemi/chromedriver'
headless_options = webdriver.ChromeOptions()
headless_options.add_argument('headless')
headless_options.add_argument('window-size=1920x1080')
headless_options.add_argument('lang=ko_KR')

driver = webdriver.Chrome(chromedriver, options = headless_options)

driver.get('https://news.v.daum.net/v/20200303110150086')

# title = driver.find_element_by_class_name('tit_view')
# print(title.text)

# content = driver.find_element_by_id('harmonyContainer')
# print(content.text)

# contents = driver.find_elements_by_css_selector('h3.tit_view')
# for content in contents:
#     print(content.text)

contents = driver.find_elements_by_css_selector('div[role="navigation"]')
for content in contents:
    print(content.text)

driver.quit()