from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

chromedriver = 'C:/Users/jinyoung/Pictures/Crawling/janjaemi/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('https://news.v.daum.net/v/20200304053015990')
loop, count = True, 0

while loop and count < 1000:
    try:
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#alex-area > div > div > div > div.cmt_box > div.alex_more > a"))
        )
        more_button = driver.find_element_by_css_selector('#alex-area > div > div > div > div.cmt_box > div.alex_more > a')
        webdriver.ActionChains(driver).click(more_button).perform()
        authors = driver.find_elements_by_css_selector('span.info_author > a')
        comment_boxes = driver.find_elements_by_css_selector('ul.list_comment >li > div > p')
        for author, comment_box in zip(authors, comment_boxes):
            print('닉네임 : ', author.text)
            print('내용 : ', comment_box.text.strip())
        count += 1
        time.sleep(1)
    except TimeoutException:
        loop = False
 
