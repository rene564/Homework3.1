x = int(input())
count = 0
a = 1
# возьмем a<=b чтобы не считать по 2 способа,
# следовательно a**2+b**2>=2a**2

while 2 * a**2 <= x:
    rest = x - a * a
    b = a
    while b * b < rest:
        b += 1
    if b * b == rest:
        count += 1
    a += 1
print(count)
