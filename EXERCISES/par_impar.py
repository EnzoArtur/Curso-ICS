'''
1,3,5,7,9

66254878272725649

'''

def calcula_par_impar(numero):
    lista_impar = '1,3,5,7,9'
    ultimo_numero = numero[-1]

    if ultimo_numero in lista_impar:
        return "impar"
    else:
        return "par"
    
res = calcula_par_impar("10")
print (res)