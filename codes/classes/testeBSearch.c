// -----------------------------------------------------------------------------
// -----------------------------------------------------------------------------

#include<stdio.h>
#include<stdlib.h>

// -----------------------------------------------------------------------------
// -----------------------------------------------------------------------------

int compareInts (const void * a, const void * b) {
  return ( *(int*)a - *(int*)b );
}

// -----------------------------------------------------------------------------
// -----------------------------------------------------------------------------

void printArray(int n, int *array) {
  printf("A = [");
  for(int i=0; i < n; i++) {
    printf("%d ", array[i]);
  }
  printf("]\n");
}

// -----------------------------------------------------------------------------
// -----------------------------------------------------------------------------

int main(int arcg, char *argv[]) {

  int values[] = { 50, 20, 60, 40, 10, 30 };
  int key;
  int* pItem;
  printArray(6, values);
  qsort (values, 6, sizeof (int), compareInts);
  printArray(6, values);

  int toSearch[] = {40, 10, 4, 5};
  int N = ((int)( sizeof((toSearch)) / sizeof(toSearch[0])));
  printf("Length = %d\n", N);

  for(int i = 0; i < N; i++) {
    key = toSearch[i];
    pItem = (int*) bsearch (&key, values, 6, sizeof (int), compareInts);
    if (pItem!=NULL)
      printf ("%d is in the array.\n", *pItem);
    else
      printf ("%d is not in the array.\n", key);
  }

  return 0;
}

// -----------------------------------------------------------------------------
// -----------------------------------------------------------------------------
