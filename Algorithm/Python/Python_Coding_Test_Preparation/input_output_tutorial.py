'''

입력

알고리즘 문제 풀이를 하려면 첫 번째로 데이터를 입력 받아야 한다.

파이썬에서 데이터를 입력받을 때는 input()을 이용한다. input()의 경우 한 줄의 문자열을 입력 받는다.

1. 여러개의 input을 받을 때는 공백으로 구분하므로 다음과 같이 받는다.

-> list(map(int, input().split()))

2. 데이터가 별로 없을 경우 그냥 변수에다가 할당해도 괜찮다

-> n, m, k = map(int, input().split())

3. 데이터가 아주 많을 때는 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 함수를 이용한다.

-> readline()을 사용하면 enter가 입력되므로 rstrip()을 사용하여 제거한다 : sys.stdin.readline().rstrip()


'''

# 데이터의 개수 입력
n = int(input())

# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

# 데이터가 많이 없을 때
n, m, k = map(int, input().split())

# 데이터가 아주 많을 때
import sys
data = sys.stdin.readline().rstrip()


'''
출력

출력을 할 때는 print()를 사용한다.

- 매개변수를 콤마(,)로 구분하며, 띄어쓰기로 구분되어 출력된다.
- print()를 사용하면 줄 바꿈이 된다.
'''
# 기본
a = "hello"
b = "wonseok"

print(a, b)

# 에러 나는 코드 : 같은 타입의 변수끼리 더해야 한다.
answer = 25
print("answer: " + answer)

# 이렇게 고쳐야 한다.
print("answer: " + str(answer))

# 또는 이렇게
print("answer: ", answer)

# f-string 문법, 중괄호({})안에 변수를 넣어서 자료형의 변환 없이도 편하게 사용 가능하다.
print(f"answer: {answer}")



