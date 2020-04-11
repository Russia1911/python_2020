
import collections
import random


def sum_tuple(numbers):
    # tuple --> sum

    total_sum = 0
    for sum_q in numbers:
        total_sum += sum_q
        return total_sum


Enterprise = collections.namedtuple('Enterprise', ['q1', 'q2', 'q3', 'q4'])

base_enterprise = {}

n = int(input("Количество предприятий: "))

for i in range(n):
    name = input(str(i+1) + '-е предприятие: ')
    profit_q1 = int(input('Прибыль за 1-й квартал: '))
    profit_q2 = int(input('Прибыль за 2-й квартал: '))
    profit_q3 = int(input('Прибыль за 3-й квартал: '))
    profit_q4 = int(input('Прибыль за 4-й квартал: '))
    base_enterprise[name] = Enterprise(
        q1=profit_q1,
        q2=profit_q2,
        q3=profit_q3,
        q4=profit_q4
    )

base_enterprise['Name1'] = Enterprise(
    q1=random.randint(100, 500),
    q2=random.randint(100, 500),
    q3=random.randint(100, 500),
    q4=random.randint(100, 500)
)

base_enterprise['Name2'] = Enterprise(
    q1=random.randint(100, 500),
    q2=random.randint(100, 500),
    q3=random.randint(100, 500),
    q4=random.randint(100, 500)
)

total_profit = ()

for name, profit in base_enterprise.items():
    print(f'Предприятие: {name} прибыль за год - {sum(profit)}')
    total_profit += profit

avg_profit_total = sum(total_profit) / len(base_enterprise)
print(f'Средняя прибыль за год для всех предприятий {avg_profit_total}')

print('Предприятия, у которых прибыль выше среднего:')

for name, profit in base_enterprise.items():
    if sum(profit) > avg_profit_total:
        print(f'{name} - {sum(profit)}')

for name, profit in base_enterprise.items():
    if sum(profit) < avg_profit_total:
        print(f'{name} - {sum(profit)}')














"ЗАДАЧА № 2 "

a = input()
b = input()
a = complex(a)
b = complex(b)
suma = a + b
mult = a * b
print(suma)
print(mult)


# Вариант 2. Определение собственного класса и перегрузка операторов:
# ООП
class Cmplx:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, obj):
        self.sumax = self.x + obj.x
        self.sumay = self.y + obj.y

    def __mul__(self, obj):
        self.multx = self.x * obj.x - self.y * obj.y
        self.multy = self.y * obj.x + self.x * obj.y


x = float(input("Введите 1-е число"))
y = float(input("Введите 2-е число"))
a = Cmplx(x, y)
x = float(input("Введите 1-е число"))
y = float(input("Введите 2-е число"))
b = Cmplx(x, y)
a + b
a * b
print('Сумма:   %.2f+%.2fj' % (a.sumax, a.sumay))
print('Произв.: %.2f+%.2fj' % (a.multx, a.multy))

# Вариант 3. Использование словарей:

a = {'x': 0, 'y': 0}
b = {'x': 0, 'y': 0}
a['x'] = float(input())
a['y'] = float(input())
b['x'] = float(input())
b['y'] = float(input())
suma = {}
mult = {}
suma['x'] = a['x'] + b['x']
suma['y'] = a['y'] + b['y']
mult['x'] = a['x'] * b['x'] - a['y'] * b['y']
mult['y'] = a['y'] * b['x'] + a['x'] * b['y']
print('Сумма:   %.2f+%.2fj' % (suma['x'], suma['y']))
print('Произв.: %.2f+%.2fj' % (mult['x'], mult['y']))