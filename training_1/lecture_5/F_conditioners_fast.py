n = int(input())
min_pows = list(map(int, input().split()))
m = int(input())
pow2price = dict()
for _ in range(m):
    power, price = map(int, input().split())
    if (power in pow2price and price < pow2price[power]) or \
            power not in pow2price:
        pow2price[power] = price
price2pow = dict()
for power in pow2price:
    if (pow2price[power] in price2pow and power > price2pow[pow2price[power]]) or \
            pow2price[power] not in price2pow:
        price2pow[pow2price[power]] = power
price_sort = sorted(price2pow)
min_pows = sorted(min_pows)

i_start = 0
sum_price = 0
for p in min_pows:
    for i_cur in range(i_start, len(price_sort)):
        if price2pow[price_sort[i_cur]] >= p:
            i_start = i_cur
            sum_price += price_sort[i_cur]
            break

print(sum_price)            
