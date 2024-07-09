n = int(input("Введите число от 3-х до 20-ти: "))
if n >= 3 and n <= 20:
    password = []
    for i in range(1, n):
        for j in range(i+1, n):
            list1 = []
            a = i + j
            if n % a == 0 and a <= n:
                list1.append(i)
                list1.append(j)
                password.extend(list1)
    result = []
    for g in password:
        g = str(g)
        result.append(g)
    result = ''.join(result)
    print(f"{result} - нужный пароль!")
else:
    print("Не удалось подобрать пароль!")

