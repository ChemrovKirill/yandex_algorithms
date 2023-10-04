def lbinsearch(L, R, check, param=None):
    while L < R:
        M = (L + R) // 2
        if check(M, param):
            R = M
        else:
            L = M + 1
    return L

N, K = map(int, input().split())
array_1 = list(map(int, input().split()))
array_2 = list(map(int, input().split()))

def check(i, number):
    return array_1[i] >= number

for number in array_2:
    search_ans = lbinsearch(0, N-1, check, param=number)
    if search_ans == 0:
        print(array_1[search_ans])
    else:
        if (array_1[search_ans] - number) < abs(array_1[search_ans - 1] - number):
            print(array_1[search_ans])
        else:
            print(array_1[search_ans - 1])
