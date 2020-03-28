

""" Задание №1 """

list_age = [0]*8
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            list_age[j-2] += 1
i = 0
while i < len(list_age):
    print(i+2, ' - ', list_age[i])
    i += 1

""" Задание №2 """

from random import random
N = 10
arr = [0]*N
even = []
for i in range(N):
    arr[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
print(arr)
print('Индексы четных элементов: ', even)

""" Задание №3 """

from random import random

N = 15
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 100)
    print(arr[i], end=' ')
print()

mn = min(arr)
mx = max(arr)
imn = arr.index(mn)
imx = arr.index(mx)
print('arr[%d]=%d arr[%d]=%d' % (imn + 1, mn, imx + 1, mx))
arr[imn], arr[imx] = arr[imx], arr[imn]
for i in range(15):
    print(arr[i],end=' ')
print()


""" Задание №4 """

from random import random

number = 15
arr = [0] * number
for i in range(number):
    arr[i] = int(random() * 20)
print(arr)

num = arr[0]
max_frq = 1
for i in range(number - 1):
    frq = 1
    for k in range(i + 1, number):
        if arr[i] == arr[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]

if max_frq > 1:
    print(max_frq, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')

""" Задание №5 """
from random import random

number = 15
arr = []
for i in range(number):
    arr.append(int(random() * 100) - 50)
print(arr)

i = 0
index = -1
while i < number:
    if arr[i] < 0 and index == -1:
        index = i
    elif arr[i] < 0 and arr[i] > arr[index]:
        index = i
    i += 1

print(index + 1, ':', arr[index])

""" Задание №6 """
from random import random

number = 10
number_list = [0] * number
for i in range(number):
    number_list[i] = int(random()*50)
    print('%3d' % number_list[i], end='')
print()

min_id = 0
max_id = 0
for i in range(1, number):
    if number_list[i] < number_list[min_id]:
        min_id = i
    elif number_list[i] > number_list[max_id]:
        max_id = i
print(number_list[min_id], number_list[max_id])

if min_id > max_id:
    min_id, max_id = max_id, min_id

summa = 0
for i in range(min_id+1, max_id):
    summa += number_list[i]
print(summa)
""" Задание №7 """
from random import random

number = 10
a = []
for i in range(number):
    a.append(int(random() * 100))
    print("%3d" % a[i], end='')
print()

if a[0] > a[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2, number):
    if a[i] < a[min1]:
        b = min1
        min1 = i
        if a[b] < a[min2]:
            min2 = b
    elif a[i] < a[min2]:
        min2 = i

print("№%3d:%3d" % (min1 + 1, a[min1]))
print("№%3d:%3d" % (min2 + 1, a[min2]))

""" Задание №8 """
M = 5
N = 4
a = []
for i in range(N):
    b = []
    s = 0
    print("%d-я строка:" % i)
    for j in range(M - 1):
        n = int(input())
        s += n
        b.append(n)
    b.append(s)
    a.append(b)

for i in a:
    print(i)


""" Задание №9 """
from random import random

M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random() * 200)
        b.append(n)
        print('%4d' % n, end='')
    a.append(b)
    print()

mx = -1
for j in range(M):
    mn = 200
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print("Максимальный среди минимальных: ", mx)
