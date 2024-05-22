# need: lista esteja ordenada
def buscaBinaria(arrayList, query):
    arrayList.sort()
    inicio = 0
    fim  = len(arrayList) - 1
    
    while(inicio <= fim):
        meio = (inicio + fim)//2
        if(arrayList[meio] == query):
            return (True, meio)
        elif (query < arrayList[meio]):
            fim = meio-1
        else:
            inicio = meio+1
    
    return (False, None)

if __name__ == "__main__":
    print("ooooopa")
    lista = ['andrezao', 'arvore', 'botswana', 'lichenstein', 'piroca']
    print(lista)
    
    # procurar um elemento que existe na lista
    ret = buscaBinaria(arrayList = lista, query="piroca")
    print(ret)
    ret = buscaBinaria(arrayList = lista, query="andrezao")
    print(ret)
    ret = buscaBinaria(arrayList = lista, query="botswana")
    print(ret)
    # procurar um elemento que nao exista na lista
    ret = buscaBinaria(arrayList = lista, query = "opaaaa")
    print(ret)