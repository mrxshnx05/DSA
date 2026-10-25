s = input()

consonants = 0

for ch in s:
    if ch != 'a' and ch != 'e' and ch != 'i' and ch != 'o' and ch != 'u' and ch != 'A' and ch != 'E' and ch != 'I' and ch != 'O' and ch != 'U':
        consonants += 1

permutations = 0

if consonants > 0:
    permutations = 1

    for i in range(1, consonants + 1):
        permutations = permutations * i

print(permutations)
