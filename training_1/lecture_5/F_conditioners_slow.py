n = int(input())
min_pows = list(map(int, input().split()))
m = int(input())
pow2price = dict()
for _ in range(m):
    power, price = map(int, input().split())
    if (power in pow2price and price < pow2price[power]) or \
            power not in pow2price:
        pow2price[power] = price

powers_sort = sorted(pow2price)
min_pows = sorted(min_pows)

i_start = 0
sum_price = 0
for p in min_pows:
    min_price = pow2price[powers_sort[-1]]
    for i_cur in range(i_start, len(powers_sort)):
        if powers_sort[i_cur] >= p:
            if pow2price[powers_sort[i_cur]] <= min_price:
                min_price = pow2price[powers_sort[i_cur]]
                i_start = i_cur
    sum_price += min_price

print(sum_price)            
