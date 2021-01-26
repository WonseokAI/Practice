'''
거스름돈

거슬러 주어야 할 최소 동전의 개수를 구하는 문제
'''
# n은 거스름 돈
n = 1260
# count는 최소 동전의 개수
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    # coin으로 거슬러 줄 수 있는 동전의 개수 세기
    count += n // coin
    n %= coin

print(count)