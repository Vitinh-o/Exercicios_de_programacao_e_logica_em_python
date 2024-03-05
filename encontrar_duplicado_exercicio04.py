"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def encontra_duplicados(lista_de_inteiros):

    lista_para_comparar = lista_de_inteiros
    lista_com_o_index_de_valores_duplicados = []
    valor_seguinte = 0
    tamanho_lista = len(lista_de_inteiros)

    for indice, valor in enumerate(lista_de_inteiros):

        if valor_seguinte <= len(lista_de_inteiros):

            lista_para_comparar = lista_de_inteiros[(indice+1):(tamanho_lista)]
            valor_seguinte+=1
            
        else:
            lista_para_comparar = []

        if valor in lista_para_comparar:

            indice = lista_para_comparar.index(valor)

            indice_da_lista_original = indice + valor_seguinte

            lista_com_o_index_de_valores_duplicados.append(indice_da_lista_original)

    if lista_com_o_index_de_valores_duplicados:

        menor_indice_duplicado = min(lista_com_o_index_de_valores_duplicados)
    
        return lista_de_inteiros[menor_indice_duplicado]
    
    else:

        return -1







for lista in lista_de_listas_de_inteiros:

    primeira_ocorrencia_de_valor_duplicado = encontra_duplicados(lista)

    print(primeira_ocorrencia_de_valor_duplicado)
