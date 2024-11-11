
# Урок 8

# Задание 1
print('Задача 1')
n = int(input('Введите количество элементов списка: '))
listN = []
for i in range(0,n):
    x = int(input('Введите элемент: '))
    listN.append(x)

listN.reverse()
print('Перевернутый список:',listN)


# Задача 2
print('Задача 2')
n = int(input('Введите количество элементов списка: '))
listN = list(map(int, input(f'Введите через пробел {n} чисел: ').split() ))
listN.insert(0, listN.pop())
print(listN)


# Задача 3
print('Задача 3')
n = int(input('Введите количество рыбаков (1 ≤ n ≤ 100): '))
m = int(input('Введите сколько одна лодка может выдержать кг. (1 ≤ m ≤ 10e6): '))
boat = 0

arrWeight = []

print(f'Количество рыбаков {n}')
print(f'Одна лодка ведержит {m} кг.')

for i in range(0, n):
     x = int(input('Введите вес рыбака кг. (1 ≤ Ai ≤ m): '))
     arrWeight.append(x)

for i in range(n):
    for j in range(n - 1):
        if arrWeight[j] > arrWeight[j + 1]:
            tmp = arrWeight[j]
            arrWeight[j] = arrWeight[j + 1]
            arrWeight[j + 1] = tmp

easy = 0
heavy = len(arrWeight) - 1

while easy <= heavy:
    if arrWeight[easy] + arrWeight[heavy] <= m:
        easy += 1
    heavy -= 1
    boat += 1


print(f'Требуеться лодок: {boat}')
    

