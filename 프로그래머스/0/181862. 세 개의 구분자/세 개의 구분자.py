def solution(myStr):
    myStr=myStr.replace("a"," ").replace("b"," ").replace("c"," ")
    answer = myStr.split()
    if answer == []:
        answer = ["EMPTY"]
    return answer