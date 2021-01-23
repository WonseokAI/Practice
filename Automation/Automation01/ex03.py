import requests

from bs4 import BeautifulSoup
'''
많은 경우에 select 한번만으로 원하는 것을 가져오지 못 할 수도 있다.
-> 인덱싱을 이용하자.
'''

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

# 필요한 부분만 자르기
td_tags = soup.select('td')[:4]

for tag in td_tags:
    print(tag.get_text())