## Descobrir qual o maior número.


primeiroNumero = int(input('Digite o primeiro numero: '))
segundoNumero = int(input('Digite o segundo numero: '))

if primeiroNumero == segundoNumero:
    print('Os numeros são iguais!')
elif primeiroNumero > segundoNumero:
    print(f'{primeiroNumero} é maior!')
else:
    print(f'{segundoNumero} é o maior!')
