# vetor estático
vetor = [3, 4, 5, 6, 7]
print(vetor)

print("---------------")

def buscaLinear(vetor, elemento) :
    retorno = -1    
    for i in range(0, len(vetor)):
        # print (vetor[i])
        if(vetor[i] == elemento) :
            return (i)
    return (retorno)

print("----------------------")
# caso de sucesso (possui o elemento)
print("* Procurando o elemento 5: ")
print(buscaLinear(vetor, elemento = 5))
# caso de falha (não possui o elemento)
print("* Procurando o elemento 50: ")
print(buscaLinear(vetor, elemento = 50))
print("----------------------")

''' 
isso 
e 
um 
comentario
'''
