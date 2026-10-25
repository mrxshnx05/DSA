n = int(input())

maximum = 0

for i in range(n):
    word = input()
    consonants = 0

    for ch in word:
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
            continue
        else:
            consonants += 1

    permutations = 0

    if consonants > 0:
        permutations = 1

        for j in range(1, consonants + 1):
            permutations = permutations * j

    if permutations > maximum:
        maximum = permutations

print(maximum)
