# BeautifulSoup - 로그인 처리

import requests as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

login_info = {
    'redirectUrl' : 'http://www.danawa.com/',
    'loginMemberType': 'general',
    'id': '',
    'password' : ''
}