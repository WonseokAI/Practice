
def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    pre = -1
    for index in range(len(arr)):
        if pre != arr[index]:
            pre = arr[index]
            answer.append(pre)

    return answer