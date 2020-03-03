from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = 'C:/Users/jinyoung/Pictures/Crawling/janjaemi/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.implicitly_wait(4)
driver.get('https://www.twitter.com')
id_field = driver.find_element_by_name("session[username_or_email]")
id_field.clear()
id_field.send_keys('id')
pw_field = driver.find_element_by_name('session[password]')
pw_field.clear()
pw_field.send_keys('pw')
pw_field.send_keys(Keys.RETURN)

time.sleep(2)

# Todo
# column 구분, csv export

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(4)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

    data = driver.find_elements_by_css_selector('div[data-testid="tweet"]')

    for item in data:
        print(item.text)

driver.quit()   