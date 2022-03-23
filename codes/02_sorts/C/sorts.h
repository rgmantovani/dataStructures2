#ifndef sorts_h
#define sorts_h

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

void swap(int *a, int *b);                            // swap values between variables
void printArray(int *v, int tam);                     // Print an array
void bubbleSort(int *v, int n, int op);               // Bubble sort
void insertionSort(int *v, int n);                    // Insertion Sort
void selectionSort(int *v, int n);                    // Selection Sort
void mergeSort(int *v, int start, int end);           // Merge Sort
void merge(int *v, int start, int middle, int end);   // Merge Sort auxiliary function

#endif /* sorts_h */

