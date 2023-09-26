N = int(input())
syn_dict = {}
for _ in range(N):
    words = input().split()
    syn_dict[words[0]] = words[1]
    syn_dict[words[1]] = words[0]

print(syn_dict[input()])
