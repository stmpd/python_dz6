#Представлен список чисел.
#Необходимо вывести элементы исходного списка,
#значения которых больше предыдущего элемента. Use comprehension.
#in
#9
#out
#[15, 16, 2, 3, 1, 7, 5, 4, 10]
#[16, 3, 7, 10]

from random import randrange

n = int(input("Введите число: "))

def func(num):
    list = [randrange(0, 20) for i in range(num)]
    print(list)

    res_ls = [list[i] for i in range(1, num) if list[i] > list[i - 1]]
    print(res_ls)



func(n)