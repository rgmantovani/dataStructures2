#include <stdio.h>

/* ---------------------------------------------------------------
 #Busca Linear
 
 Testa todas as posições até encontrar o elemento desejado, ou
   procura sem sucesso até chegar ao final do vetor.
 
 @Parâmetros:
 - v é o vetor
 - n é o tamanho do vetor
 - elem é o elemento que se deseja procurar
  
 @Retorno:
 - a posição do elemento ou -1 caso não encontre
---------------------------------------------------------------*/

int buscaLinear(int *v, int n, int elem) {
  for(int i = 0; i < n; i++) {
    if(elem == v[i]) {
      return i;
    }
  }
  return -1;
}

/* ---------------------------------------------------------------
 #Busca Ordenada
 
 Testa todas as posições até encontrar o elemento desejado, ou até
 que o valor da posição testada for maior do que o elemento, ou
 procura sem sucesso até chegar ao final do vetor.
 
 @Parâmetros:
 - v é o vetor
 - n é o tamanho do vetor
 - elem é o elemento que se deseja procurar
  
 @Retorno:
 - a posição do elemento ou -1 caso não encontre
---------------------------------------------------------------*/

int buscaOrdenada(int *v, int n, int elem) {
  for(int i = 0; i < n; i++) {
    // achou
    if(elem == v[i]) {
      return i;
    }
    // achou numero maior do que o desejado
    if(v[i] > elem) {
      return -1;
    }
  }
  // percorreu todo o vetor
  return -1;
}

/* ---------------------------------------------------------------
 #Busca Binária
 
 Utiliza divisão e conquista. Testa sempre o elemento médio na
 metade do intervalo válido na iteração.
 
 @Parâmetros:
 - v é o vetor
 - n é o tamanho do vetor
 - elem é o elemento que se deseja procurar
  
 @Retorno:
 - a posição do elemento ou -1 caso não encontre
---------------------------------------------------------------*/

int buscaBinaria(int *v, int n, int elem) {

  int inicio = 0;
  int fim = n-1;
  int meio;
  
  while(inicio <= fim) {
    meio = (inicio+fim)/2;
    if(v[meio] == elem) {
      return meio;
    } else if(elem < v[meio]) {
      fim = meio-1;
    } else {
      inicio = meio+1;
    }
  }
  return -1;
}

/* -------------------------------------------- */
/* -------------------------------------------- */

int main(int argc, const char * argv[]) {
  
  int random[] = {1, 25, 3, 30, 41, 27, 17, 4, 2, 5};
  int sorted[] = {1, 2, 4, 5, 17, 25, 27, 30, 31, 41};

  int index1, index2, index3;
  
  index1 = buscaLinear(random, 10, 41);
  index2 = buscaOrdenada(sorted, 10, 41);
  index3 = buscaBinaria(sorted, 10, 41);
  
  printf("Indice de busca linear: %i\n",   index1);
  printf("Indice de busca ordenada: %i\n", index2);
  printf("Indice de busca binaria: %i\n",  index3);

  return 0;
}

/* -------------------------------------------- */
/* -------------------------------------------- */

