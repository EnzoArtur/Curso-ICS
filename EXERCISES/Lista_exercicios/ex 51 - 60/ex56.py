lista_palavras = ["eu quero ir para belo horizonte"]

for numero in range(len(lista_palavras)):
    lista_palavras[numero] = lista_palavras[numero].replace("belo horizonte", "São Romão")

print(lista_palavras)