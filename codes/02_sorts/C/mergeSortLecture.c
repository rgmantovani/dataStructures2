#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */

void printArray(int *v, int size) {
  printf("V = [");
  for (int i = 0; i < size; i++) {
    printf("%d ", v[i]);
  }
  printf("]\n");
}

void printDebug(int *v, int start, int end) {
  printf("V = [");
  for (int i = start; i < end+1; i++) {
    printf("%d ", v[i]);
  }
  printf("]\n");
}

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */

void merge(int *v, int start, int middle, int end) {

  // Alocar dinamicamente um vetor auxiliar só para os elementos da recursão
  int vecSize = (end - start)+1;
  int *aux = malloc(vecSize * sizeof(int));

  int p1 = start;
  int p2 = middle + 1;
  int j, n, k, i = 0;

  while(p1 <= middle && p2 <= end) {
    // copia para o vetor auxiliar o menor valor entre v[p1] e v[p2]
    if(v[p1] < v[p2]) {
      aux[i++] = v[p1++];
    } else {
      aux[i++] = v[p2++];
    }
  }

  // Se P1 > meio, sobraram elementos em P2
  if(p1 > middle) {
    //sobram End - p2 + 1 elementos
    n = end - p2 + 1;
    // copia os elementos que sobraram da parte da direita (p2)
    for(j = 0; j < n; j++) {
      aux[i++] = v[p2++];
    }
  } // Senão, P2 > Fim, sobraram elementos em P1
  else {
    // sobram Middle - p1 + 1 elementos
    n = middle - p1 + 1;
    // copia os elementos que sobraram da parte da esquerda (p1)
    for(j = 0; j < n; j++) {
      aux[i++] = v[p1++];
    }
  }

  // copiar elementos do aux para v
  // aux e v podem ter tamanhos diferentes
  j = 0;
  k = start;
  while(j < vecSize) {
    v[k] = aux[j];
    j++; k++;
  }
  free(aux);
}

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */

void mergeSort(int *v, int start, int end) {

  int middle;
  if(start < end) {
    middle = (int)floor((start + end)/2);
    mergeSort(v, start, middle);
    mergeSort(v, (middle+1), end);
    merge(v, start, middle, end);
  }
}

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */

int main(int argc, const char * argv[]) {

  int v[] = {45, 36, 2, 8, 0, 1, 23, 2, 2, 10};
  printArray(v, 10);
  mergeSort(v, 0, 9);
  printArray(v, 10);
  return 0;
}

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */
