def solution(myString, pat):
    i = myString.rfind(pat)
    answer = myString[:i+len(pat)]
    return answer