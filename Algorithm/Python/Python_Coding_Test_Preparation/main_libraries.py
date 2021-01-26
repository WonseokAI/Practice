'''

표준 라이브러리 : 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리

표준 라이브러리 링크 : https://docs.python.org/ko/3/library/index.html

반드시 알아야 하는 라이브러리

1. 내장 함수 : print(), input()과 같은 기본 입출력 기능부터 sorted()와 같은 정렬 기능을 포함하고 있는 기본 내장 라이브러리
2. itertools : 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리. ex) 순열과 조합 라이브러리
3. heapq: 힙(heap) 기능을 제공하는 라이브러리. 우선순위 큐 기능을 구현하기 위해 사용한다.
4. bisect: 이진 탐색(Binary Search) 기능을 제공하는 라이브러리.
5. collections: 덱(deque), 카운터(Counter)등의 유용한 자료구조를 포함하고 있는 라이브러리.
6. math : 필수적인 수학적 기능을 제공하는 라이브러리. ex) 팩토리얼, 제곱근, 최대공약수, 삼각함수등의 함수부터 수학적 상수까지 포함한다.

'''

'''
내장 함수

- 별도의 import 없이 바로 사용할 수 있는 함수
- 가장 기본적이고 필수적인 기능을 포함한다.
- 예를 들어, print()와 input()

'''

# sum() : 리스트와 같은 iterable 객체가 입력으로 주어졌을 때, 모든 원소의 합을 반환한다.
result = sum([1,2,3,4,5])

# min() : 2개 이상의 파라미터에 대해서 가장 작은 값을 반환한다.
result = min(7, 3, 5, 2)

# max() : 2개 이상의 파라미터에 대해서 가장 큰 값을 반환한다.
result = max(7, 3, 5, 2)

# eval() : 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다.
result = eval("(3 + 5) * 7")

# sorted() : iterable 객체가 들어왔을 때, 정렬된 결과를 반환, reverse 속성으로 정렬 기준을 명시할 수 있다.

# 오름차순
result = sorted([9,1,8,5,4])
print(result)

# 내림차순
result = sorted([9,1,8,5,4], reverse = True)
print(result)

# 튜플도 가능하다
# 예: 원소를 튜플의 두 번째 원소를 기준으로 내림차순 정렬
result = sorted([('A', 64), ('T', 90), ('G', 78), ('R', 354)])

# sort() : 리스트와 같은 iterable 객체는 기본으로 sort() 함수를 내장하고 있다.
data = [9,34,7,2,10]
data.sort()


'''
Itertools

- 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리이다.
- 자주 사용되는 클래스는 permutations, combinations 등이 있다.

'''
from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C']

# data에서 3개를 뽑아 나열하는 모든 경우 구하기
result = list(permutations(data, 3))

# data에서 2개를 뽑는 모든 조합 구하기
result = list(combinations(data, 2))

# product() : iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열(원소 중복)
# data에서 중복을 포함하여 2개를 뽑아 나열하는 모든 경우의 수
result = list(product(data, repeat=2))

# combinations_with_replacement() : iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우의 수(원소 중복)
# data에서 중복을 허용하고 2개를 뽑는 모든 조합 구하기
result = list(combinations_with_replacement(data, 2))

'''
heapq

- Heap 기능을 위한 라이브러리
- 우선순위 큐 기능을 구현하고자 할 때 사용된다.
- PriorityQueue를 이용하여 구현할 수 있지만, heapq가 보통 더 빠르다.
- 파이썬의 힙은 최소 힙(Min Heap)으로 구성되어 있으므로 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간 복잡도 O(NlogN)에 오름차순 정렬이 된다.

- 삽입 : heapq.heappush()
- 꺼내기 : heapq.heappop()

- 파이썬에서는 최대 힙을 제공하지 않으므로, heapq를 이용하여 최대 힙을 구현해야 할 때는 원소의 부호를 임시로 변경하는 방식을 사용한다.
-> 힙에 원소를 삽입하기 전에 잠시 부호를 반대로 바꾸고, 힙에서 원소를 꺼낸 뒤에 다시 원소의 부호를 바꾸면 된다.
'''

'''
bisect

- 이진 탐색을 위한 라이브러리
- 정렬된 배열에서 특정한 원소를 찾아야 할 때 효과적으로 사용된다.
- bisect_left(), bisect_right()함수가 중요하게 사용된다 : 시간 복잡도 O(logN)
1. bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
2. bisect_right(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

- 특히 위의 두 함수는 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구하고자 할 때, 효과적으로 사용된다. : O(logN)
'''

'''
collections

- 유용한 자료구조를 제공하는 표준 라이브러리
- 유용한 클래스 : deque, Counter

- 보통 deque를 사용해 큐를 구현한다.
- deque에서는 리스트 자료형과 다르게 인덱싱, 슬라이싱 등의 기능은 사용할 수 없다.
- 하지만 리스트 자료형과는 다르게 연속적으로 나열된 데이터의 시작 부분이나 끝부분에 데이터를 삽입하거나 삭제할 때 매우 효과적이다.
- deque는 스택이나 큐의 기능을 모두 포함한다.
- deque에서 첫 번째 원소를 제거할 때 popleft()를 사용하며, 마지막 원소를 제거할 때 pop()을 사용한다.
- 첫 번째 인덱스에 원소를 삽입할 때, appendleft(a)를 사용하며, 마지막 인덱스에 원소를 삽입할 때 append(a)를 사용한다.

- deque를 큐로 사용할 때, 삽입은 append(), 삭제는 popleft()를 사용하면 된다.

- Counter는 등장 횟수를 세는 기능을 제공한다. Iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지 알려준다.
'''

'''
math

- 수학적인 기능을 포함하고 있는 라이브러리
- ex) factorial(x) = x!
- ex) sqrt(x) = x의 제곱근
- ex) gcd(a, b) = a와 b의 최대 공약수
- ex) 자연 상수 e 또는 pi
'''