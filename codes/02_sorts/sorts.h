#ifndef sorts_h
#define sorts_h

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

void generateArray(int *v, int n, int option);        // Generate an array
void printArray(int *v, int n);                       // Print an array
void bubbleSort(int *v, int n);                       // Bubble sort
void insertionSort(int *v, int n);                    // Insertion Sort
void selectionSort(int *v, int n);                    // Selection Sort
void mergeSort(int *v, int start, int end);           // Merge Sort
void merge(int *v, int start, int middle, int end);   // Merge Sort - auxiliar function
void quickSort(int *v, int start, int end);           // Quick Sort
int partition(int *v, int start, int end);            // Quick Sort - auxiliar function
void heapSort(int *v, int n);                         // Heap Sort
void heapify(int *v, int n, int i);                   // Heap Sort -  auxiliar function

#endif /* sorts_h */
