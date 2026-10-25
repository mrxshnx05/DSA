n = int(input())
L = int(input())
R = int(input())
A = list(map(int, input().split()))

level = 0
maximum = 0
minimum = 0

for i in range(n):
    if L <= A[i] <= R:
        level += 1
    else:
        level -= 1

    if level > maximum:
        maximum = level

    if level < minimum:
        minimum = level

print(maximum, minimum)
