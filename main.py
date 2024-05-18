
peso = str(input('Informe o peso:')).replace(',','.')
altura = str(input('Informe a altura:')).replace(',','.')

peso = float(peso)
altura = float(altura)

imc = peso/(altura**2)    #outra forma: imc = peso/(altura * altura)

print(f'{imc:,.1f}') #deixar o resultado com 1 casa decimal(variavel:,.1f)

if imc < 18.5:
    print(f'Abaixo do peso normal({imc:,.1f}).')
elif imc >= 18.5 and imc <= 24.9:
    print(f'Peso normal({imc:,.1f}).')
elif imc >= 25 and imc <= 29.9:
    print(f'Excesso de peso({imc:,.1f}).')
elif imc >= 30 and imc <= 34.9:
    print(f'Obsidade Classe I({imc:,.1f}).')
elif imc >= 35 and imc <= 39.9:
    print(f'Obsidade Classe II({imc:,.1f}).')
else: 
    print(f'Obsidade Classe III({imc:,.1f}).')
