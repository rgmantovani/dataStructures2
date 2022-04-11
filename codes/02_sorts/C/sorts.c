#include "sorts.h"

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */

void swap(int *a, int *b) {
  int tmp = *a;
  *a = *b;
  *b = tmp;
}

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

void bubbleSort(int *v, int n, int op) {

  if(op != 1 && op !=2) {
    printf("Warning: not valid option. Please, choose 1 (ascending) or 2 (descending).\n");
    return;
  }

  bool changed = true;

  while(changed) {
    changed = false;
    for(int i = 0; i < n-1; i++) {

      // op == 1 -> ascending order
      if(op == 1) {
        if(v[i] > v[i+1]) {
          swap(&v[i], &v[i+1]);
          changed = true;
        }
      // op == 2 (descending order)
      } else {
        if(v[i] < v[i+1]) {
          swap(&v[i], &v[i+1]);
          changed = true;
        }
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
    while(j>=0 && chosen < v[j]) {
      v[j+1] = v[j];
      j = j-1;
    }

    /* move the element to the new place */
    v[j+1] = chosen;
  }
}

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */

void merge(int *v, int start, int middle, int end) {

  int *temp;
  int i, j, k;
  int p1, p2;
  int vecSize;

  bool finished1 = false;
  bool finished2 = false;

  vecSize = (end - start) + 1;

  p1 = start;
  p2 = middle + 1;

  temp = (int*) malloc(vecSize * sizeof(int));

  if(temp != NULL) {

    for(i = 0; i < vecSize; i++) {

      if(!finished1 && !finished2) {
        if(v[p1] < v[p2]) {
          temp[i] = v[p1++];
        } else {
          temp[i] = v[p2++];
        }

        /* checking if any sub vector finished */
        if(p1 > middle){finished1 = true;}
        if(p2 > end)   {finished2 = true;}

      } else {
        /* copying the remaining elements */
        if(!finished1)
          temp[i] = v[p1++];
        else
          temp[i] = v[p2++];
      }
    }
    /* copying elements from temp to v */
    for(j=0, k=start; j<vecSize; j++, k++) {
      v[k] = temp[j];
    }

  } //if
  free(temp);
}

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */

void mergeSort(int *v, int start, int end) {

  int middle;

  if(start < end) {
    /* find the element in the middle */
    middle = (int)floor((start + end)/2);
//    printf("middle = %d\n", middle);

    /* calling recursively fot both halves of the original
     array - reducing the problem */
    mergeSort(v, start, middle);
    mergeSort(v, (middle+1), end);

    /* merging them in the correct order */
    merge(v, start, middle, end);
  }
}

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */

void quickSort(int *v, int start, int end) {
  int pivot;
  if(end > start) {
    pivot = makePartitions(v, start, end);
    quickSort(v, start, pivot-1);
    quickSort(v, pivot+1, end);
  }
}

int makePartitions(int *v, int start, int end) {

  int left = start;
  int right  = end;
  int pivot     = v[start];

  while(left < right) {
    while(v[left] <= v[pivot]) {
      left++;
    }
    while(v[right] > pivot) {
      right--;
    }
    if(left < right) {
      swap(&v[left], &v[right]);
    }
  }
  v[start] = v[right];
  v[right] = pivot;
  retorna(right);
}

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */
