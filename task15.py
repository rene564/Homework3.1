# если у числа есть делитель, больший чем его квадратный корень,
# то у него обязательно есть и второй делитель (парный ему),
# который меньше или равен квадратному корню
n = int(input())
for num in range(2, n + 1):
    is_prime = True
    d = 2
    while d * d <= num:
        if num % d == 0:
            is_prime = False
            break
        d += 1
    if is_prime:
        print(num)