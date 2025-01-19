def solution(arr):

    number = 0
    while True:
        answer = []
        for a in arr:
            if a%2==0 and a >= 50 :
                answer.append(int(a/2))
            elif a%2==1 and a<=50 :
                answer.append(a*2+1)
            else:
                answer.append(a)
            
        if answer == arr:
            break
            result = number
        else :
            number+=1
            arr = answer
    return number
