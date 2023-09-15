def read_numbers():
    numbers = []
    while True:
        n = int(input())
        if n == -2e9:
            break
        else:
            numbers.append(n)
    return numbers

def seq_type(numbers):
    pos_const = True
    pos_asc = True
    pos_wasc = True
    pos_desc = True
    pos_wdesc = True
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i-1]:
            pos_asc = False
            pos_wasc = False
            pos_const = False
        elif numbers[i] == numbers[i-1]:
            pos_asc = False
            pos_desc = False
        else:
            pos_desc = False
            pos_wdesc = False
            pos_const = False
    if pos_const:
        return "CONSTANT"
    elif pos_asc:
        return "ASCENDING"
    elif pos_desc:
        return "DESCENDING "
    elif pos_wasc:
        return "WEAKLY ASCENDING"
    elif pos_wdesc:
        return "WEAKLY DESCENDING"
    else:
        return "RANDOM"

print(seq_type(read_numbers()))