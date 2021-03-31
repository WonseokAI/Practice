
def solution(s):
    ss = s.lower()
    py = [0,0]
    for char in ss:
        if char is 'p':
            py[0] += 1
        elif char is 'y':
            py[1] += 1
    if py[0] - py[1] is 0:
        return True
    else:
        return False