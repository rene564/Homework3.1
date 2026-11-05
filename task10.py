a = float(input())
count = 0
while a != 0:
    b = float(input())
    if b == 0:
        break
    if b < a:
        count += 1
    a = b
print(count)