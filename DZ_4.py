import random
import timeit
import cProfile
import sys

# Написать два алгоритма нахождения i-го по счёту простого числа.
def test(num, n=10000):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    print(f'Количество простых чисел в диапазоне до {n}: {len(res)}')

    assert num < len(res)
    return res[num - 1]


def eratosthenes_sieve(n):
    count = 1
    start = 3
    end = 4 * n

    sieve = [i for i in range(start, end) if i % 2 != 0]
    prime = [2]

    if n == 1:
        return 2

    while count < n:

        for i in range(len(sieve)):

            if sieve[i] != 0:
                count += 1

                if count == n:
                    return sieve[i]

                j = i + sieve[i]

                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]

        prime.extend([i for i in sieve if i != 0])

        start, end = end, end + 2 * n
        sieve = [i for i in range(start, end) if i % 2 != 0]

        for i in range(len(sieve)):

            for num in prime:

                if sieve[i] % num == 0:
                    sieve[i] = 0
                    break

# py -m timeit -n 100 -s "import Lesson_4_Task_2" "Lesson_4_Task_2.eratosthenes_sieve(10)"
# "Lesson_4_Task_2.eratosthenes_sieve(10)"
# 100 loops, best of 5: 4.69 usec per loop
# "Lesson_4_Task_2.eratosthenes_sieve(100)"
# 100 loops, best of 5: 201 usec per loop
# "Lesson_4_Task_2.eratosthenes_sieve(1000)"
# 100 loops, best of 5: 17.3 msec per loop
# Предположительно, алгоритм сложности O(n**2). Увеличение количества чисел в 10 раз
# увеличивает время выполнения приблизительно в 100 раз

# cProfile.run('eratosthenes_sieve(10)')
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:31(eratosthenes_sieve)
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:36(<listcomp>)
# cProfile.run('eratosthenes_sieve(100)')
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:31(eratosthenes_sieve)
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:36(<listcomp>)
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:58(<listcomp>)
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:61(<listcomp>)
# cProfile.run('eratosthenes_sieve(1000)')
# 1    0.022    0.022    0.023    0.023 Lesson_4_Task_2.py:31(eratosthenes_sieve)
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:36(<listcomp>)
# 2    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:58(<listcomp>)
# 2    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:61(<listcomp>)
# Время выполнения нарастает


def search_prime(n):
    count = 1
    number = 1
    prime = [2]

    if n == 1:
        return 2

    while count != n:
        number += 2

        for num in prime:
            if number % num == 0:
                break
        else:
            count += 1
            prime.append(number)

    return number

# py -m timeit -n 100 -s "import Lesson_4_Task_2" "Lesson_4_Task_2.search_prime(10)"
# "Lesson_4_Task_2.search_prime(10)"
# 100 loops, best of 5: 3.35 usec per loop
# "Lesson_4_Task_2.search_prime(100)"
# 100 loops, best of 5: 187 usec per loop
# "Lesson_4_Task_2.search_prime(1000)"
# 100 loops, best of 5: 18 msec per loop
# Сложность близка к O(n**2)
# Скорость работы обоих алгоритмов на данных объемах данных практически одинакова.

# cProfile.run('search_prime(1000)')
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:97(search_prime) 10
# 1    0.000    0.000    0.000    0.000 Lesson_4_Task_2.py:97(search_prime) 100
# 1    0.019    0.019    0.019    0.019 Lesson_4_Task_2.py:97(search_prime) 1000
# Время выполнения нарастает. Рекурсий нет.


# ВЫВОД:
# Сложность алгоритмов и время их работы приблизительно одинаковые.


# --------------------------------------------------------------------------------------
# №1 создание матрицы двумя циклами
def m_create_2_for(range_raw, range_coll):
    matrix = [[random.randint(1, 100) for _ in range(1, range_coll)] for _ in range(1, range_raw)]


# timeit m_create_2_for(10, 10):
# 100 loops, best of 3: 157 usec per loop

# timeit m_create_2_for(100, 100):
# 100 loops, best of 3: 18.5 msec per loop

# timeit m_create_2_for(150, 150):
# 100 loops, best of 3: 41.2 msec per loop

# cProfile.run('m_create_2_for(10, 10)')
# 1 0.000 0.000 0.000 0.000 task_01.py: 8(speed_test)

# cProfile.run('m_create_2_for(100, 100)')
# 1    0.000    0.000    0.025    0.025 task_01.py:8(speed_test)

# cProfile.run('m_create_2_for(1000, 1000)')
#  1    0.000    0.000    2.634    2.634 task_01.py:8(speed_test)

# Итог: сложность данного алгоритма = О(N**2)

# --------------------------------------------------------------------------------------
# №2 Создание матрицы 1 циклом
def m_create_1_for(size_matrix):
    matrix = []
    temp_array = []

    for i in range(1, (size_matrix ** 2) + 1):
        val = random.randint(1, 100)

        if i % size_matrix == 0:
            temp_array.append(val)
            matrix.append(temp_array)
            temp_array = []
        else:
            temp_array.append(val)
    print(matrix)


# timeit m_create_1_for(10):
# 100 loops, best of 3: 438 usec per loop

# timeit m_create_1_for(100):
# 100 loops, best of 3: 25.9 msec per loop

# timeit m_create_1_for(150):
# 100 loops, best of 3: 55.6 msec per loop

# cProfile.run("m_create_1_for(10)")
# 1 0.000 0.000 0.000 0.000 task_01.py: 33(m_create_1_for)

# cProfile.run("m_create_1_for(100)")
# 1    0.006    0.006    0.039    0.039 task_01.py:33(m_create_1_for)

# cProfile.run("m_create_1_for(1000)")
# 1    0.663    0.663    3.401    3.401 task_01.py:33(m_create_1_for)

# Итог: сложность данного алгоритма = О(N**2), при этом данный алгоритм медленнее чем алгоритм №1

# ---------------------------------------------------------------------------------------------
# №3 Создание матрицы рекурсией
sys.setrecursionlimit(2000)

def m_create_recursion(range_raw, range_coll, coll_count=0, f_matrix = []):
    matrix = []
    if coll_count + 1 == range_coll:
        for _ in range(range_raw):
            matrix.append(random.randint(1, 100))
        f_matrix.append(matrix)
        return f_matrix
    else:
        for _ in range(range_raw):
            matrix.append(random.randint(1, 100))
        coll_count += 1
        f_matrix = m_create_recursion(range_raw, range_coll, coll_count)
        f_matrix.append(matrix)
        return f_matrix

# timeit m_create_recursion(10, 10):
# 100 loops, best of 3: 198 usec per loop

# timeit m_create_recursion(100, 100):
# 100 loops, best of 3: 20 msec per loop

# timeit m_create_recursion(150, 150):
#100 loops, best of 3: 45.4 msec per loop

# cProfile.run('m_create_recursion(10, 10)')
# 10/1    0.000    0.000    0.001    0.001 task_01.py:77(m_create_recursion)

# cProfile.run('m_create_recursion(100, 100)')
# 100/1    0.006    0.000    0.031    0.031 task_01.py:77(m_create_recursion)

# cProfile.run('m_create_recursion(1000, 1000)')
# 1000/1    0.583    0.001    3.165    3.165 task_01.py:79(m_create_recursion)

# Итог: сложность данного алгоритма так же О(N**2), при этом на небольшом размере матрицы (10, 10) он медленнее
# алгоритмов №1 и №2, но на размере 100 и >, он выигрывает по времени у алгоритма №2, но для таких значений требуется
# увеличения стека для рекурсии, так как при стандартном размере стек переполняется, не давая алгоритму
# завершить действие.

# По итогу проведения оценки скорости работы алгоритмов, с уверенностью можно сказать, что наиболее выгодным алгоритмом
# для создания матриц является алгоритм №1