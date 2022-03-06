#Calculadora de IMC

print('Calculadora de IMC')
print(' ')
altura = float(input('Qual é a sua altura em cm? '))
peso = float(input('Qual é o seu peso em kg? '))

IMC = round(peso / (altura/100)**2,1)

if IMC < 18.5:
    print(f'Seu IMC é de  {IMC}, e é classificado como Magreza.')

elif IMC >= 18.5 and IMC < 24.9:
    print(f'Seu IMC é de  {IMC}, e é classificado como Normal.')

elif IMC >=25 and IMC < 29.9:
    print(f'Seu IMC é de  {IMC}, e é classificado como Sobrepeso.')

elif IMC >= 30 and IMC < 39.9:
    print(f'Cuidado! Seu IMC é de  {IMC}, e é classificado como Obesidade.')

else:
    print(f'Procure um médico, seu IMC é de {IMC}, e é classificado como Obesidade Grave!')