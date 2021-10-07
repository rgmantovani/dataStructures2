
#include "sorts.h"

/* ------------------------------------------------------- */
// Imprime vetor
/* ------------------------------------------------------- */

void printArray(int *v, int tam) {
  printf("V = [");
  for(int i = 0; i < tam; i++) {
    printf("%d ", v[i]);
  }
  printf("]\n");
}

/* ------------------------------------------------------- */
// Ordenação por borbulhamento
/* ------------------------------------------------------- */

void bubbleSort(int *v, int n) {

  int aux;
  bool changed = true;
  
  while(changed) {
    changed = false;
    for(int i = 0; i < n-1; i++) {
      if(v[i] > v[i+1]) {
        aux    = v[i+1];
        v[i+1] = v[i];
        v[i]   = aux;
        changed = true;
      }
    }
  }
}

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */
