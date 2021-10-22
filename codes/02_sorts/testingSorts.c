#include <stdio.h>
#include "sorts.h"

int main(int argc, const char * argv[]) {
  
  int v1[] = {45, 36, 2, 8, 0, 1, 23, 2, 2, 10};
  int v2[] = {45, 36, 2, 8, 0, 1, 23, 2, 2, 10};
  int v3[] = {45, 36, 2, 8, 0, 1, 23, 2, 2, 10};
  int v4[] = {45, 36, 2, 8, 0, 1, 23, 2, 2, 10};
  int v5[] = {45, 36, 2, 8, 0, 1, 23, 2, 2, 10};
  int v6[] = {45, 36, 2, 8, 0, 1, 23, 2, 2, 10};

  int N = 10;
  
  printArray(v4, N);
  
  bubbleSort(v1, N);
  printArray(v1, N);

  selectionSort(v2, N);
  printArray(v2, N);

  insertionSort(v3, N);
  printArray(v3, N);
  
  mergeSort(v4, 0, N-1);
  printArray(v4, N);
 
  quickSort(v5, 0, N-1);
  printArray(v5, N);
 
  heapSort(v6, N);
  printArray(v6, N);
  
  return 0;
  
}
