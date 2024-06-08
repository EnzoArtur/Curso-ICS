multiplica = [3,7]

def duplicar_elementos(aumentar_valor):
    aumentar_quantidade_de_elemntentos = []
    for elemento in aumentar_valor:
        aumentar_quantidade_de_elemntentos.append(elemento)
        aumentar_quantidade_de_elemntentos.append(elemento)
    return aumentar_quantidade_de_elemntentos

lista = duplicar_elementos(multiplica)
print(lista)