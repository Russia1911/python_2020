from random import random  # 6 Задача

""" Задание № 1 """

while True:
    user_input = input("Знак (+,-,/,*): ")
    if user_input == '0':
        break
    if user_input in ('+', '-', '/', '*'):
        x = float(input("x="))
        y = float(input("y="))
        if user_input == '+':
            print("%.2f" % (x+y))
        elif user_input == '-':
            print("%.2f" % (x-y))
        elif user_input == '*':
            print("%.2f" % (x*y))
        elif user_input == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")


""" Задание № 2 """

n = int(input())
even = odd = 0
while n > 0:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    n = n//10
print("четных - %d, нечетных - %d" % (even, odd))

""" Задание № 3 """

n = int(input())
m = 0
while n > 0:
    m = m*10 + n % 10
    n = n//10
print(m)

""" Задание № 4 """
n = int(input())
e = 1
s = 0
for i in range(n):
    s += e
    e /= -2
print(s)


""" Задание № 5 """

for i in range(32, 128):
    print("%4d-%s" % (i, chr(i)), end='')
    if i % 10 == 0:
        print()

print()

""" Задание № 6 """

random_age = round(random() * 100)
i = 1
print("Компьютер загадал число. Отгадайте его. У вас 10 попыток")
while i <= 10:
    u = int(input(str(i) + '-я попытка: '))
    if u > random_age:
        print('Много')
    elif u < random_age:
        print('Мало')
    else:
        print('Вы угадали с %d-й попытки' % i)
        break
    i += 1
else:
    print('Вы исчерпали 10 попыток. \n Число которое загодал компьютер = ', random_age)



""" Задание № 7 """
n = int(input())
s = 0
for i in range(1, n + 1):
    s += i
m = n * (n + 1) // 2
print(s)
print(m)


""" Задание № 8 """
n = int(input("Сколько будет чисел? "))
d = int(input("Какую цифру считать? "))
count = 0
for i in range(1, n + 1):
    m = int(input("Число " + str(i) + ": "))
    while m > 0:
        if m % 10 == d:
            count += 1
        m = m // 10

print("Было введено %d цифр %d" % (count, d))

""" Задание № 9 """
n = int(input())
max_s = 0
max_m = 0
while n != 0:
    m = n
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    if s > max_s:
        max_s = s
        max_m = m
    n = int(input())
print('Число', max_m, 'имеет максимальную сумму цифр:', max_s)


""" Рекурсия  9 """


def recur_method(quantity, step , highest_number , max_sum ):
    summ = 0
    try:
        numb = input("Введите число = ")
        for i in numb:
            summ += int(i)
        if summ > max_sum:
            max_sum = summ
            highest_number = numb
        step += 1
        if step == quantity:
            return f"Наибольшее число = {highest_number} , сумма цифр {max_sum}"
        else:
            return recur_method(quantity, step , highest_number , max_sum )
    except ValueError:
        print(" Ошибка --- введите числа , а не строку ")

