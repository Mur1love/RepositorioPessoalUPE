n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media < 4:
    print(f'Media: {media}, REPROVADO!')
    print('Conceito: E')
elif media < 6:
    print(f'Media: {media}, REPROVADO!')
    print('Conceito: D')
elif media < 7.5:
    print(f'Media: {media}, APROVADO!')
    print('Conceito: C')
elif media < 9:
    print(f'Media: {media}, APROVADO!')
    print('Conceito: B')
elif media <= 10:
    print(f'Media: {media}, APROVADO!')
    print('Conceito: A')