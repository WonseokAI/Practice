
def solution(a, b):
    date = [31,29,31,30,31,30,31,31,30,31,30,31]
    answer = [ "THU","FRI", "SAT", "SUN","MON", "TUE", "WED"]
    days = sum(date[:a-1])+b if a > 1 else b
    return answer[days%7]