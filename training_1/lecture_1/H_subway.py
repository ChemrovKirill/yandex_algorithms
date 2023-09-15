a = int(input())
b = int(input())
n = int(input())
m = int(input())

t1_left = n + (n-1) * a
t2_left = m + (m-1) * b
t_left = max(t1_left, t2_left)
t1_right = n + (n+1) * a
t2_right = m + (m+1) * b
t_right = min(t1_right, t2_right)
if t_right < t_left:
    print(-1)
else:
    print(t_left, t_right)
