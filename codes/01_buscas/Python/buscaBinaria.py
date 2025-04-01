# vetor estático
vetor = [3, 4, 5, 6, 7]
print(vetor)

print("---------------")

def buscaBinaria(vetor, elemento):
    inicio = 0
    fim = len(vetor)-1
    while(inicio <= fim):
        meio = (inicio + fim)//2
        # print(meio)
        if(vetor[meio] == elemento):
            return (meio)
        elif (vetor[meio] < elemento):
            inicio = meio + 1
        else:
            fim = meio - 1
    return (-1)

print("----------------------")
# caso de sucesso (possui o elemento)
print("* Procurando o elemento 5: ")
print(buscaBinaria(vetor, elemento = 5))
# caso de falha (não possui o elemento)
print("* Procurando o elemento 50: ")
print(buscaBinaria(vetor, elemento = 50))
print("----------------------")
