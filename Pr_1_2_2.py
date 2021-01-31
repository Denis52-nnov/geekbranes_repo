# Форматирование

Time = int(input('Введите время в секундах: '))

h = (Time//3600)%24
m = (Time//60)%60
s = Time%60
if h < 10:
    h = str('0' + str(h))
else:
    h = str(h)
if m < 10:
    m = str('0' + str(m))
else:
    m = str(m)
if s <10:
    s = str('0' + str(s))
else:
    s = str(s)
fstring = f'{h}:{m}:{s}'
print(fstring)

