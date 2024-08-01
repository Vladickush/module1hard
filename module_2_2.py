
first = int(input('first = '))
second = int(input('second = '))
third = int(input('third = '))

if first == second and second == third:
    print (3, ' совпадения')
elif first == second or first == third or second == third:
    print(2, ' совпадения')
else:
    print(0, ' совпадений')