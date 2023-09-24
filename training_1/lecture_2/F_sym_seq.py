def make_symmetric_slow(seq):
    """ O(len(seq)**2) """
    to_add = []
    N = len(seq)
    for i in range(N):
        if seq[i] != seq[N-1]:
            to_add.append(seq[i])
        else:
            il = i+1
            ir = N-2
            is_sym = True
            while il < ir:
                if seq[il] != seq[ir]:
                    is_sym = False
                il += 1
                ir -= 1
            if is_sym:
                break
            else:
                to_add.append(seq[i])
    return to_add[::-1]

N = int(input())
seq = input().split()
to_add = make_symmetric_slow(seq)
print(len(to_add))
print(*to_add)
