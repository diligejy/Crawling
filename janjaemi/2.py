from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# chromedriver = 'C:/Users/jinyoung/Pictures/Crawling/janjaemi/chromedriver'
#driver = webdriver.Chrome(chromedriver)

# PhantomJS
# phantomjs_file = 'C:/Users/jinyoung/Pictures/Crawling/janjaemi/phantomjs'
# driver = webdriver.PhantomJS(phantomjs_file)
# driver.get('https://python.org')

# Headless Chrome
chromedriver = 'C:/Users/jinyoung/Pictures/Crawling/janjaemi/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chromedriver, options=options)

search = driver.find_element_by_id('id-search-field')
search.clear()
search.send_keys('Python')
search.send_keys(Keys.RETURN)

data = driver.find_elements_by_css_selector('#content > div > section > form > ul > li > h3 > a')
for item in data:
    print(item.text)