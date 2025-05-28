# -----------------------------------------------------------------------------------
# Função: Busca Binária
# Params: 
#         - arrayList: lista de elemntos a serem verificados
#         - query: valor de consulta
# Retorno:
#         - (True/False, índice): Tupla se achou ou não, e o índice da posição onde 
#           o elemento existe
# -----------------------------------------------------------------------------------
def buscaBinaria(arrayList, query):
    
    # Inicialização das variáveis
    arrayList.sort()
    inicio = 0
    fim  = len(arrayList) - 1
    
    # Laço principal
    while(inicio <= fim):
        meio = (inicio + fim)//2
        if(arrayList[meio] == query):
            # retorno se houve sucesso (achou o elemento)
            return (True, meio)
        elif (query < arrayList[meio]):
            fim = meio-1
        else:
            inicio = meio+1
    
    # retorno em condiçoes de falha
    return (False, None)

# -----------------------------------------------------------
# Casos de teste da função
# -----------------------------------------------------------

if __name__ == "__main__":

    # lista com elementos
    lista = ['andrezao', 'arvore', 'botswana', 'lichenstein']
    print(lista)
    
    # procurar elementos que existem na lista
    ret = buscaBinaria(arrayList = lista, query="andrezao")
    print(ret)
    ret = buscaBinaria(arrayList = lista, query="botswana")
    print(ret)

    # procurar um elemento que nao exista na lista
    ret = buscaBinaria(arrayList = lista, query = "opaaaa")
    print(ret)
    
# -----------------------------------------------------------
# -----------------------------------------------------------