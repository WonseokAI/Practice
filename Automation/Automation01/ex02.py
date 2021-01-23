import requests

from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

# html parser로 rating_page안에 있는 html code를 정리한다.
soup = BeautifulSoup(rating_page, 'html.parser')

# prettify() 함수로 출력할 것을 더 이쁘게 만들어준다.
print(soup.prettify())

# select() 함수를 이용하여 원하는 태그를 가져온다. css 선택자를 parameter로 받는다.
print(soup.select('title'))
print(soup.select('table'))

# example : 프로그램 이름 가져오기
# td태그 이면서 class 이름이 program인 태그
program_title_tags = soup.select('td.program')

program_titles = []

for tag in program_title_tags:
    # get_text()를 사용하면 태그의 text를 가져온다.
    program_titles.append(tag.get_text())

# 우리가 원하는 태그들중에 가장 위에 있던 태그 가져오기
print(soup.select_one('td.program'))

'''

해당 웹 사이트에 있는 전화번호 모두 가져오기
https://workey.codeit.kr/orangebottle/index
'''

# HTML 코드 받아오기
response = requests.get("https://workey.codeit.kr/orangebottle/index")

# BeautifulSoup 타입으로 변환
soup = BeautifulSoup(response.text, 'html.parser')

# "phoneNum" 클래스를 가진 span 태그 선택하기
phone_number_tags = soup.select('span.phoneNum')

phone_numbers = []

# 텍스트 추출해서 리스트에 추가하기
for tag in phone_number_tags:
    phone_numbers.append(tag.get_text())

# 출력 코드
print(phone_numbers)









