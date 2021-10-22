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

// Function to swap the the position of two elements
void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */

void bubbleSort(int *v, int n) {

  bool changed = true;
  
  while(changed) {
    changed = false;
    for(int i = 0; i < n-1; i++) {
      if(v[i] > v[i+1]) {
        swap(&v[i], &v[i+1]);
        changed = true;
      }
    }
  }
}

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */

void selectionSort(int *v, int n) {
  
  int i, j, min;
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
      swap(&v[i], &v[min]);
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
  if (end > start) {
    /* finding the pivot */
    pivot = partition(v, start, end);
    /* calling recursively for both paritions */
    quickSort(v, start, pivot-1); // [start, pivot-1]
    quickSort(v, pivot+1, end);   // [pivot+1, end]
  }
}

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */

int partition(int *v, int start, int end) {
  
  int left, right, pivot;
  
  left  = start;
  right = end;
  pivot = v[start];
  
  while(left < right) {
    
    /* increase left index */
    while(v[left] <= pivot) {
      left++;
    }
    
    /* decrease right index */
    while(v[right] > pivot) {
      right--;
    }
    
    /* swap elements in the left and right
      positions */
    if(left < right) {
      swap(&v[left], &v[right]);
    }
  }
  
  /* select the pivot's correct position */
  v[start] = v[right];
  v[right] = pivot;

  return(right);
}

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */

void heapSort(int *v, int n) {
  
  int i;
  
  /* build heap (rearrange array) */
  for(i = n/2 - 1; i >=0; i--) {
    heapify(v, n, i);
  }
  
  /* One by one extract an element from heap */
  for(i = n-1; i > 0; i--) {
    /* Move current root to end */
    swap(&v[0], &v[i]);
    /* call max heapify on the reduced heap */
    heapify(v, i, 0);
  }
}

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */

void heapify(int *v, int n, int i) {
  
  int largest = i;
  int left    = 2 * i + 1;
  int right   = 2 * i + 2;
  
  /* if left child is larger than root */
  if(left < n && v[left] > v[largest]) {
    largest = left;
  }
  
  /* if right child is larger than largest so far */
  if(right < n && v[right] > v[largest]) {
    largest = right;
  }
  
  /* if largest is not root */
  if(largest != i) {
    swap(&v[i], &v[largest]);
    
    /* recursively heapify the affected sub-tree*/
    heapify(v, n, largest);
  }
}

/* ------------------------------------------------------- */
/* ------------------------------------------------------- */
