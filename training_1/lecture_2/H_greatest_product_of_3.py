def find_max_prodof3_slow(seq):
    max_prod = seq[0] * seq[1] * seq[2]
    best_numbers = (seq[0], seq[1], seq[2])
    for i in range(len(seq)):
        for j in range(len(seq)):
            if j == i:
                continue
            for k in range(len(seq)):
                if k == i or k == j:
                    continue
                prod = seq[i] * seq[j] * seq[k]
                if prod > max_prod:
                    max_prod = prod
                    best_numbers = (seq[i], seq[j], seq[k])
    return best_numbers


def find_max_prodof3_fast(seq):
    if len(seq) == 3:
        return seq
    max_pos_1, max_pos_2, max_pos_3 = 0, 0, 0
    max_neg_1, max_neg_2= 0, 0
    min_neg_1, min_neg_2, min_neg_3 = 0, 0, 0
    zeros_num = 0
    for i in range(len(seq)):
        if seq[i] == 0:
            zeros_num += 1
        elif seq[i] > 0:
            if seq[i] > max_pos_1:
                max_pos_3 = max_pos_2
                max_pos_2 = max_pos_1
                max_pos_1 = seq[i]
            elif seq[i] > max_pos_2:
                max_pos_3 = max_pos_2
                max_pos_2 = seq[i]
            elif seq[i] > max_pos_3:
                max_pos_3 = seq[i]
        elif seq[i] < 0:
            # abs maxes
            if seq[i] < max_neg_1:
                max_neg_2 = max_neg_1
                max_neg_1 = seq[i]
            elif seq[i] < max_neg_2:
                max_neg_2 = seq[i]
            # abs mins
            if min_neg_1 == 0:
                min_neg_1 = seq[i]
            elif min_neg_2 == 0:
                min_neg_2 = seq[i]
            elif min_neg_3 == 0:
                min_neg_3 = seq[i]
                min_neg_3, min_neg_2, min_neg_1 = sorted([min_neg_1, min_neg_2, min_neg_3])
            else:
                if seq[i] > min_neg_1:
                    min_neg_3 = min_neg_2
                    min_neg_2 = min_neg_1
                    min_neg_1 = seq[i]
                elif seq[i] > min_neg_2:
                    min_neg_3 = min_neg_2
                    min_neg_2 = seq[i]
                elif seq[i] > min_neg_3:
                    min_neg_3 = seq[i]
    if max_pos_1 == 0: # no positive numbers
        if zeros_num:
            return max_neg_1, max_neg_2, 0
        else:
            return min_neg_1, min_neg_2, min_neg_3
    sub_seq = [max_neg_1, max_neg_2, max_pos_3, max_pos_2, max_pos_1]
    if zeros_num:
        sub_seq.append(0)
    return find_max_prodof3_slow(sub_seq)


seq = list(map(int, input().split()))
print(*find_max_prodof3_fast(seq))

                
# Stress test
"""
import random
while True:
    randvals = []
    for i in range(7):
        randvals.append(random.randint(-10, 10))
    # randvals = [-3, 9, -7, 2, -6, 5, 7]
    slowans = sorted(find_max_prodof3_slow(randvals))
    fastans = sorted(find_max_prodof3_fast(randvals))
    print(*randvals)
    if slowans == fastans:
        print("OK")
    else:
        print("WA", f"{fastans=}", f"{slowans=}")
        break
"""
