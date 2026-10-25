A = int(input())
B = int(input())

result = 0
place = 1

while A > 0 or B > 0:
    bit1 = A % 2
    bit2 = B % 2

    if bit1 == 1 or bit2 == 1:
        result = result + place

    A = A // 2
    B = B // 2
    place = place * 2

print(result)
