# Определение номера дня, в который будет достигнут заданный результат

a = int(input('Введите результат первого дня: '))
b = int(input('Введите желаемый результат: '))
c = 1
while a < b:
        a = a * 1.1
        c += 1
else:
    print('Спортсмен достигнет желаемого результата на', c, 'день')
