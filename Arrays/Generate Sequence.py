n = int(input())
initial = list(map(int, input().split()))

A = [0] * n

for i in range(n):
    if i < 6:
        A[i] = initial[i]
    else:
        A[i] = A[i - 1] + A[i - 2]

for i in range(n):
    print(A[i], end=" ")
