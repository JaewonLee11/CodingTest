def solution(my_string, s, e):
    answer = ''.join(my_string[e-1::s])
    return answer