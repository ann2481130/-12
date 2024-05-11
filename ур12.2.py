N = int(input('Введите целое число:'))
a = []
for i in range(N):
    a.append(int(input('Введите целое число:')))
print(f'Массив: {a}')
a.sort()
print(f'Массив отсортированный:{a}')
b = len(set(a))
print(f'Количество различных элементов: {b}')