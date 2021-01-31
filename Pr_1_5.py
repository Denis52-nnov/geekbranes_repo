# Расчет финансового результата

earn = float(input('Введите значение выручки: '))
cost = float(input('Введите значение издержек: '))

fin_rez = float(earn - cost)
if fin_rez < 0:
    print('Получен убыток')
else:
    rent = float(earn / cost)
    print('Рентабельность:', '%.2f' % rent)
    sotr = float(input('Введите количество сотрудников: '))
    ern_to_sotr = float(earn / sotr)
    print('Прибыль на одного сотрудника составила:', '%.2f' % ern_to_sotr)

