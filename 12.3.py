N = int(input('Введите количество сотрудников:'))
sph =[]
hs =[]
res = []
for i in range(N):
    sph.append(int(input('Введите сколько сотрудник получает за час:')))
    hs.append(int(input('Введите сколько сотрудник отработал часов/мес:')))
    r = sph[i] * hs[i]
    res.append(r)
res.sort()
print(res)