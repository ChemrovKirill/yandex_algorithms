N, Linput = map(int, input().split())

def sequence(params):
    x, d, a, c, m = params
    seq = [x]
    for i in range(Linput-1):
        x = x + d
        seq.append(x)
        d = (a*d + c) % m
    return seq

seqs = []
for _ in range(N):
    params = map(int, input().split())
    seqs.append(sequence(params))


def check(m, seq, number):
    if seq[m] >= number:
        return True

def lbinsearch(L, R, check, seq, number):
    while L < R:
        M = (L + R) // 2
        if check(M, seq, number):
            R = M
        else:
            L = M + 1
    return L


def cntless(seq, x):
    ans = lbinsearch(0, len(seq) - 1, check, seq, x)
    if seq[ans] < x:
        return len(seq)
    return ans


def median(seq1, seq2):
    L = min(seq1[0], seq2[0])
    R = max(seq1[-1], seq2[-1])
    while L < R:
        M = (L + R) // 2
        left = cntless(seq1, M) + cntless(seq2, M)
        right = len(seq1) - cntless(seq1, M+1) + len(seq2) - cntless(seq2, M+1)
        if left <= len(seq1) - 1 and right <= len(seq1):
            return M
        if right > len(seq1):
            L = M + 1
        if left > len(seq1) - 1:
            R = M - 1
    return L

for i in range(N):
    for j in range(i+1, N):
        print(median(seqs[i], seqs[j]))
