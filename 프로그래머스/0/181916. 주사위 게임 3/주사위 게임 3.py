from collections import Counter

def solution(a, b, c, d):
    answer = 0
    values = [a, b, c, d]
    unique_values = sorted(set(values))

    if len(unique_values) == 1:
        answer = 1111 * a
    
    elif len(unique_values) == 2:
        counter = Counter(values)
        number_list = [item for item, count in counter.items() if count == 2]
        
        if len(number_list) == 2:
            answer = (number_list[0] + number_list[1]) * abs(number_list[0] - number_list[1])
        else:
            max_value = max(counter, key=counter.get)
            min_value = min(counter, key=counter.get)
            answer = (10 * max_value + min_value) ** 2

    elif len(unique_values) == 3:
        counter = Counter(values)
        two_items = [item for item, count in counter.items() if count == 2]
        other_items = [item for item, count in counter.items() if count == 1]
        answer = other_items[0] * other_items[1]

    else:
        answer = unique_values[0]

    return answer