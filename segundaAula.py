'''Exercicio 1
nome = ('Munir Assis\n')

print(nome)'''

'''Exercicio 2
a = 3
b = 5
multi1 = 2*a
multi2 = 3*b
result = multi1 * multi2
print(result)'''

'''Exercicio 3

nota1 = float(input("coloque a nota 1 ="))
nota2 = float(input('coloque a nota 2 ='))
nota3 = float(input('coloque a nota 3 ='))

soma = nota1 + nota2 + nota3
print(f'soma = {soma:.1f}')

divisão = soma / 3
print(f'divisão = {divisão:.1f}')'''

'''Exercicio 5

metros = float(input('coloque os metros = '))
milimetros = (metros * 10000)
print(f'{metros} metros em milimetros é = {milimetros:.0f}\n')'''

'''Exercicio 6'''

dias = int(input('coloque os dias = '))
segundosDias = (dias * 86400)

horas = int(input('coloque as horas = '))
segundosHoras = (horas * 3600)

minutos = int(input('coloque os minutos = '))
segundosMinutos = (minutos * 60)

segundos = int(input('coloque os segundos = '))

somasSegundos = (segundosDias + segundosHoras + segundosMinutos + segundos)
print(f'{dias} dias, {horas} horas, {minutos} mintos, {segundos} segundos, em segundos são = {somasSegundos}')
