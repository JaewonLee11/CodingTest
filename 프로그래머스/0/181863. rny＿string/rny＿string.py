def solution(rny_string):
    answer = ''
    strlist = []
    strlist = list(rny_string)
    print(strlist)
    for i in range(len(strlist)):
        if  strlist[i] == "m":
            strlist[i] = "rn"
    answer = "".join(strlist)
    return answer