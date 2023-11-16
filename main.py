from random import randint
from math import gcd #greatest common devisor

def NOD(a, b):
    if(a==0 or b==0):
        return a+b
    if a > b:
        return NOD(a%b,b)
    else:
        return NOD(b%a, a)

while True:
    try:
        print("Введите целое значение a:")
        a=int (input())
        break
    except ValueError:
        print("Ошибка: неправильно введены данные")

while True:
    try:
        print("Введите целое значение b:")
        b=int (input())
        break
    except ValueError:
        print("Ошибка: неправильно введены данные")

rez_1=NOD(a, b)
rez_2=gcd(a,b)
print(f'НОД чисел {a}, {b} равен {rez_1} = {rez_2}')


# for _ in range(1000):
#     a=randint(1,10000)
#     b=randint(1,10000)
#     rez_1=NOD(a, b)
#     rez_2=gcd(a,b)
#     # if rez_1!=rez_2:
#     #     print('+')
#     print(f'НОД чисел {a}, {b} равен {rez_1}')

