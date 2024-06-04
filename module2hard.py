random_number = int(input('Ведите число от 3 до 20 :'))

result = []
for i in range(1, random_number):
    if random_number < 3 or random_number > 20:
        print('Неверное число')
        break
    for j in range(1, random_number // 2 + 1):

        if random_number % (i + j) == 0 and i != j and i != j // 2:
            result.append(i)
            result.append(j)
print(result)
