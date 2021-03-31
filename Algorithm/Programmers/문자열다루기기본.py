
def solution(s):

    answer = True

    if len(s)==4 or len(s)==6:
        for element in s:
            if not element.isdigit():
                return False
    else:
        return False

    return answer