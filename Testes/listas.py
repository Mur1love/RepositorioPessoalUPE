frutas = ['Banana', 'Maça', 'Caqui', 'Girimum', 'Melancia']

print(frutas[2])
print(frutas)
frutas[1] = 'Banana'
print(frutas)
frutas.append('Abacate')
print(frutas)
frutas.pop(2)
print(frutas)
print(frutas.pop(-1))
print(frutas)
print(len(frutas))


print('Aqui começa o for: ')

for fruta in frutas:
    if fruta != 'Banana':
        print(fruta)
