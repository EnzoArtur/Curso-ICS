ano = int(input('digite o ano: '))

if ( ano % 4 == 0 and ano % 100 !=0 ) or (ano % 400 == 0):
    print(ano , ' e um ano bissexto ')

else:
    print(ano , 'nao e um ano bissexto ')