s = input()

consonants = 0

for ch in s:
    if ch not in "aeiouAEIOU":
        consonants += 1

permutations = 0

if consonants > 0:
    permutations = 1

    for i in range(1, consonants + 1):
        permutations = permutations * i

print(permutations)