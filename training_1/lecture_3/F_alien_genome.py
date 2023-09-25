def find_pairs(genome):
    pairs = list()
    for i in range(len(genome) - 1):
        pairs.append(genome[i] + genome[i+1])
    return pairs

genome_pairs_1 = find_pairs(input())
genome_pairs_2_set = set(find_pairs(input()))

closeness = 0
for pair in genome_pairs_1:
    if pair in genome_pairs_2_set:
        closeness += 1
print(closeness)
