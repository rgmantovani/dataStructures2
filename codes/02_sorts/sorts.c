#include "sorts.h"

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */

void printArray(int *v, int tam) {
  printf("Array = [");
  for(int i = 0; i < tam; i++) {
    printf("%d ", v[i]);
  }
  printf("]\n");
}

/* ------------------------------------------------------- */
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

void selectionSort(int *v, int n) {
  
  int i, j, min, aux;
  for(i = 0; i < n-1; i++) {
    min = i;
    
    /* search for the minimum value according to
     the i position */
    for(j = i+1; j < n; j++) {
      if(v[j] < v[min]) {
        min = j;
      }
    }
    
    /* swap elements of positions i and min */
    if(i != min) {
      aux    = v[i];
      v[i]   = v[min];
      v[min] = aux;
    }
  }
}

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */

void insertionSort(int *v, int n) {

  int i, j, chosen;
  for(i = 1; i < n; i++) {
    
    chosen = v[i];
    j = i-1;
    
    /* search for the values that can swift one
     position forward */
    while(j>=0 & chosen < v[j]) {
      v[j+1] = v[j];
      j = j-1;
    }
    
    /* move the element to the new place */
    v[j+1] = chosen;
  }
}

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */
