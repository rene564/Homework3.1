while True:
    x = int(input("Введите число: "))
    if x >= 0 and int(x ** 0.5) ** 2 == x:
        print("Число является полным квадратом")
        break
    else:
        print("Число не является полным квадратом")