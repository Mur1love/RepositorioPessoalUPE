x = int(input('n1: '))
y = int(input('n2: '))
z = int(input('n3: '))

if x < y:
    if x < z:
        print(f'{x} é o menor número!')
    else:
        print(f'{z} é o menor número!')
else:
    if y < z:
        print(f'{y} é o menor número!')
    else:
        print(f'{z} é o menor número!')
