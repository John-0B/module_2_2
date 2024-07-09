first = int(input('Введите первое число:_'))
second = int(input('Введите второе число:_'))
third = int(input('Введите третье число:_'))
if first == second and second == third and third == first:
    print('Три числа равны')
elif first == second or second == third or third == first:
    print('Два числа равны')
else:
    print('Нет равных чисел')
