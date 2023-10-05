N, L = map(int, input().split())

seqs = []
for _ in range(N):
    seqs.append(list(map(int, input().split())))

def median(seq1, seq2):
    seq = sorted(seq1 + seq2)
    return seq[L-1]

for i in range(N):
    for j in range(i+1, N):
        print(median(seqs[i], seqs[j]))
