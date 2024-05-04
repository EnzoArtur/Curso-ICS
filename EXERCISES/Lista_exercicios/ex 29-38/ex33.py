nota1 = float(input('digite a sua primeira nota: '))
nota2 = float(input('digite a sua segunda nota: '))
nota3 = float(input('digite a sua terceira nota: '))
nota4 = float(input('digite a sua quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4 ) /4

if media >= 7:
    print('Parabens, voce esta aprovado com media' , media)
elif 5 <= media < 7:
    print('voce esta de recuperacao com media ' , media)
else:
    print('voce esta reprovado com media ' , media)