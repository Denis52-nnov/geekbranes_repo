# Поиск наибольшей цифры в числе

a = int(input('Введите число: '))
b = a % 10 # выбираем из введенного числа последнюю цифру, с нейбудем сравнивать остальные
a = a // 10 # уменьшаем введенное число на одну цифру - последнюю, т.к. ее записали в переменную b

while a > 0: # записываем цикл для числа, которое больше 0
    if a % 10 > b: # если остаток от деления на 10(последняя цифра в a=a//10) больше, чем значение в переменной b,которое мы занесли ранее, то
        b = a % 10 # заносим новое значение в переменную b
    a = a // 10
print(b)
