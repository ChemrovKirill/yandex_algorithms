a = int(input())
b = int(input())
c = int(input())

def lbinsearch(L, R, check):
    while L < R:
        M = (L + R) // 2
        if check(M):
            R = M
        else:
            L = M + 1
    return L

def check(d):
    if (a*2 + b*3 + c*4 + d*5) * 2 >= (a + b + c + d) * 7 :
        return True
    
print(lbinsearch(0, 3*(a+b+c), check))
