a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = b * b - 4 * a * c

if delta < 0: 
    print('Delta menor que zero!')
elif delta == 0:
    raiz = -b / (2 * a)
    print('x1 =', raiz, 'x2= ', raiz)
else:
    raiz_positiva = (-b + delta**0.5) / (2 * a)
    raiz_negativa = (-b - delta**0.5) / (2 * a)
    print('x1=', raiz_positiva, 'x2=', raiz_negativa)
