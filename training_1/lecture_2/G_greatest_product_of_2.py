def find_max_prodof2(seq):
    if len(seq) == 2:
        return sorted(seq)
    max_pos_1 = 0
    max_pos_2 = 0
    max_neg_1 = 0
    max_neg_2 = 0 
    for i in range(len(seq)):
        if seq[i] >= 0:
            if seq[i] > max_pos_1:
                max_pos_2 = max_pos_1
                max_pos_1 = seq[i]
            elif seq[i] > max_pos_2:
                max_pos_2 = seq[i]
        else:
            if abs(seq[i]) > abs(max_neg_1):
                max_neg_2 = max_neg_1
                max_neg_1 = seq[i]
            elif abs(seq[i]) > abs(max_neg_2):
                max_neg_2 = seq[i]
    if max_pos_1 * max_pos_2 > max_neg_1 * max_neg_2:
        return max_pos_2, max_pos_1
    else:
        return max_neg_1, max_neg_2

seq = list(map(int, input().split()))
print(*find_max_prodof2(seq))
