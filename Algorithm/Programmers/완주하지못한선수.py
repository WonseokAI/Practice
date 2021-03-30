
def solution(participant, completion):
    answer = ''
    h = dict()
    for e in participant:
        if e in h:
            h[e] += 1
        else:
            h[e] = 1

    for e in completion:
        if h[e] == 1:
            del h[e]
        else:
            h[e] -= 1
    answer = list(h.keys())[0]
    return answer