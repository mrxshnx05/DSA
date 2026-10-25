n = int(input())
A = list(map(int, input().split()))

for i in range(n):
    count = 0

    if i == 0:
        left = A[n - 1]
    else:
        left = A[i - 1]

    if i == n - 1:
        right = A[0]
    else:
        right = A[i + 1]

    if left > A[i]:
        count += 1

    if right > A[i]:
        count += 1

    print(count, end=" ")
