
def solution(a, b):
    abSum = 0
    for i in range(min(a,b),max(a,b)+1):
        abSum += i
    return abSum