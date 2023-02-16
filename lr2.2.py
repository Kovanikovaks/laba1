a = int(input('Введите место в вагоне:'))
if a not in range(1, 55):
    print('неправильный номер места')
elif a % 2 == 0 and a in range(1, 37):
    print('Место', a, 'находится в купе сверху')
elif a % 2 == 1 and a in range(1, 37):
    print('Место', a, 'находится в купе снизу')
elif a % 2 == 0 and a in range(37, 55):
    print('Место', a, 'находится c боку сверху')
elif a % 2 == 1 and a in range(37, 55):
    print('Место', a, 'находится с боку снизу')
