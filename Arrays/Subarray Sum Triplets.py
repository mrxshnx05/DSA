n = int(input())
A = list(map(int, input().split()))

count = 0

for i in range(n - 2):
    if A[i] + A[i + 2] == A[i + 1]:
        count += 1

print(count)
