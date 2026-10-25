n = int(input())

if n < 0:
    n = -n

while n >= 10:
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10

    n = total

print(n)
