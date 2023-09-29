N, K = map(int, input().split())
numbers = list(map(int, input().split()))

L = 0
R = -1
cnt = 0
cursum = 0
while L < len(numbers) and R < len(numbers):
    if L != R and cursum > K:
        cursum -= numbers[L]
        L += 1
    else:
        R += 1
        if R >= len(numbers):
            break
        cursum += numbers[R]
    if cursum == K:
        cnt += 1

print(cnt)
