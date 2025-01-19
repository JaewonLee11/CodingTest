def solution(num_list):
    answer = 0
    while any(i != 1 for i in num_list):
        for i in range(len(num_list)):
            if num_list[i]==1:
                continue
            elif num_list[i] % 2 == 0:
                num_list[i] //= 2
                answer+=1
            else:
                num_list[i]=(num_list[i]-1)//2
                answer+=1
    return answer