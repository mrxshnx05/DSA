n = int(input())
A = list(map(int, input().split()))

total = 0
for i in range(n):
    total += A[i]

prefix = 0
count = 0

for i in range(n - 1):
    prefix += A[i]
    suffix = total - prefix

    if (prefix - suffix) % 2 == 0:
        count += 1

print(count)
