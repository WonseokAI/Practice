import requests

''' response 받기 '''
response = requests.get("https://google.com")

# 성공하면 200, 실패하면 500.
print(response)

# html code를 받음
print(response.text)


''' 여러 페이지의 html code 가져오기 '''
# https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0
rating_pages = []
for i in range(5):
    url = "https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex={}".format(i)
    response = requests.get(url)
    rating_page = response.text
    rating_pages.append(rating_page)

# 가져온 총 페이지 수
print(len(rating_pages))

# 첫 번째 페이지의 HTML 코드
print(rating_pages[0])


''' 해당 주소에서 2010년 1월부터 2018년 12월까지 모든 달에 대해, 1주차~5주차 페이지를 순서대로 리스트에 넣기 '''
# https://workey.codeit.kr/ratings/index
ratings_pages = []

for year in range(2010, 2019):
    for month in range(1, 13):
        for weekIndex in range(0, 5):
            url = "https://workey.codeit.kr/ratings/index?year={}&month={}&weekIndex={}".format(year, month, weekIndex)
            response = requests.get(url)
            rating_pages.append(response.text)

# 가져온 총 페이지 수
print(len(rating_pages))

# 첫 번째 페이지의 HTML 코드
print(rating_pages[0])