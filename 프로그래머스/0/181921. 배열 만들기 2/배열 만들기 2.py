def solution(l, r):
    answer = []
    for n in range(l, r + 1):
        if all(digit in "05" for digit in str(n)):
            answer.append(n)
    return answer if answer else [-1]