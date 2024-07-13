n = int(input('введите число от 3 до 20: '))
numbers_p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
a = 0
b = 0
result = []
for a in numbers_p:
    if a < n:
        for b in numbers_p:
            if b > a and b < n and n % (a + b) == 0:
                result.append(a)
                result.append(b)
print('result: ', *result)

