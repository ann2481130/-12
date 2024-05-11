def cmp(x):
    return x % 3
a = [34, -5, 0, 12, 45, 8, 32, -17, 1, 99]
a.sort(key=cmp)
print(a)