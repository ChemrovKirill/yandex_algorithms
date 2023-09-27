from string import ascii_uppercase

N = int(input())

stress_dict = dict()
for _ in range(N):
    word_stress = input()
    word = word_stress.lower()
    if word not in stress_dict:
        stress_dict[word] = set()
    stress_dict[word].add(word_stress)

mistakes = 0
task_words = input().split()
for word_stress in task_words:
    word = word_stress.lower()
    stresses = 0
    for c in word_stress:
        if c in ascii_uppercase:
            stresses += 1
    if word in stress_dict:
        if word_stress not in stress_dict[word]:
            mistakes += 1
    elif stresses != 1:
        mistakes += 1

print(mistakes)
