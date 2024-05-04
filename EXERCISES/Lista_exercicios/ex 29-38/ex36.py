def verificar_palindromo(texto):
    texto = texto.replace('' , ' ').replace(', ', ' ').replace('. ' ,' ').replace(' !' , ' ').replace('? ', ' ')

    return texto == texto[::-1]

texto_usuario = input('insira uma palavra ou frase: ')

if verificar_palindromo(texto_usuario):
    print('e um palindromo')

else:
    print('nao e um palindromo')