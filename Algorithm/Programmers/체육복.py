
def solution(n, lost, reserve):
    reallost = set(lost) - set(reserve)
    realreser = set(reserve) - set(lost)
    for data in realreser:
        if data-1 in reallost:
            reallost.remove(data-1)
        elif data+1 in reallost:
            reallost.remove(data+1)
    return n - len(reallost)