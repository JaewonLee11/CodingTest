def solution(my_string, target):
    a = len(my_string)
    b = len(target)
    answer = 0
    for i in range(0,a-b+1):
        if my_string[i:i+b]==target:
            answer = 1
    return answer