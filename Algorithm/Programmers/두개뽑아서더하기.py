
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    # 중복 제거를 위해 set사용
    return sorted(list(set(answer)))