# BeautifulSoup
# BeautifulSoup 사용 스크랩핑(1) - 기본 사용법

from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title> The Dormouse's story</title>
    </head>
    <body>
        <h1> This is h1 area </h1>
        <h2> This is h2 area </h2>
        <p class = "title"><b>The Dormouse's story</b></p>
        <p class = "story">Once upon a time there were three little psisters.
            <a href = "http://example.com/elsie" class = "sister" id = "link1">Elsie</a>
            <a href = "http://example.com/elsie" class = "sister" id = "link2">Lacie</a>
            <a href = "http://example.com/elsie" class = "sister" id = "link3">Elsie</a>
            <a data-io ="link3" href = "http://example.com/elsie" class = "sister" id = "link4">Elsie</a>
        </p>
        <p class = "story">
            story...
        </p>
    </body>
</html>


"""
# bs4 초기화
soup = BeautifulSoup(html, 'html.parser')

# 타입 확인
print(type(soup))
print('prettify', soup.prettify)

# h1 태그 접근
h1 = soup.html.body.h1
print('h1', h1)

# p 태그에 접근
p1 = soup.html.body.p
print('p', p1)

# 다음 태그
p2 = p1.next_sibling.next_sibling
print('p2', p2)

# 텍스트 출력
print('h1 > ' , h1.string)

# 텍스트 출력2
print('p1 >>', p1.string)

# 함수확인
# print(dir(p2))

# 다음 엘리먼트 확인
# print(list(p2.next_element))

# 중요
link2 = soup.find_all('a', class_='sister')
print(link2)

for t in link2:
    print(t)

# 처음 발견한 a 태그 선택
link3 = soup.find('a')

print()
print(link3)
print(link3.string)
print(link3.text)

# 다중 조건
link4 = soup.find("a", {"class" : "sister", "data-io" : "link3"})

print()
print(link4)
print(link4.text)
print(link4.string)

# 예제3(select, select_one)
# css 선택자 : select, select_one
# 태그로 접근 : find 계열
# select : 태그 + 클래스 + 자식선택자

link5 = soup.select_one('p.title > b')
print()
print(link5)
print(link5.text)
print(link5.string)

# #(sharp)은 ID
link6 = soup.select_one('a#link1')
print()
print(link6)
print(link6.text)
print(link6.string)

#
link7 = soup.select_one("a[data-io='link3']")

print()
print(link7)
print(link7.text)
print(link7.string) #. : 클래스, # : id

 # 선택자에 맞는 전체 선택
link8 = soup.select('p.story > a')
print()
print(link8)
# print(link8.text)
# print(link8.string) #. : 클래스, # : id

# 
link9 = soup.select('p.story > a:nth-of-type(2)')

print()
print(link9)
# print(link9.text)
# print(link9.string) #. : 클래스, # : id

print()
for t in  soup.select("p.story"):
    temp = t.find_all("a")
    
    if temp:
        for v in temp:
            print('>>>>>', v)
            print('>>>>>', v.string)
    else :
        print('-----', t)
        print('-----', t.string)