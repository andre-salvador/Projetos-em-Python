altura = float(input('Qual sua altura: '))
peso = float(input('Qual é seu peso: '))

if altura > 3:
    altura = altura / 100

imc = peso / (altura * altura)
print(f'Seu IMC é de {imc}')

if imc < 18.5:
    print('Você está abaixo do peso!')

elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal!')

elif imc >= 25 and imc < 30:
    print('Você está acima do peso!')

elif imc >= 30 and imc < 40:
    print('Você está com obsidade!')

else:
    print('Você está com obsidade mórbida')