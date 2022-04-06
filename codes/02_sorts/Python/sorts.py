# ---------------------------------------------------------------------------------------
# Bubble Sort
# ---------------------------------------------------------------------------------------
def bubbleSort(array):
    for k in range(len(array)-1,0,-1):
        for i in range(k):
            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]

# ---------------------------------------------------------------------------------------
# Short Bubble Sort
# ---------------------------------------------------------------------------------------
def shortBubbleSort(array):
    exchanges = True
    k = len(array)-1
    while k > 0 and exchanges:
       exchanges = False
       for i in range(k):
           if array[i]>array[i+1]:
               exchanges = True
               array[i], array[i+1] = array[i+1], array[i]
       k = k-1

# ---------------------------------------------------------------------------------------
# Selection Sort
# ---------------------------------------------------------------------------------------

def selectionSort(array):
    for k in range(len(array)-1,0,-1):
        positionOfMax=0
        for location in range(1,k+1):
            if array[location]>array[positionOfMax]:
                positionOfMax = location
        if positionOfMax != k:
                array[k], array[positionOfMax] = array[positionOfMax], array[k]

# ---------------------------------------------------------------------------------------
# Insertion Sort
# ---------------------------------------------------------------------------------------

def insertionSort(array):
   for index in range(1,len(array)):
     currentvalue = array[index]
     position = index
     while position>0 and array[position-1]>currentvalue:
         array[position]=array[position-1]
         position = position-1
     array[position]=currentvalue

# ---------------------------------------------------------------------------------------
# Merge Sort
# ---------------------------------------------------------------------------------------
# https://codereview.stackexchange.com/questions/154135/recursive-merge-sort-in-python

def merge(left, right):
    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def mergeSort(array):
    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half  = len(array) // 2
    left  = mergeSort(array[:half])
    right = mergeSort(array[half:])
    return merge(left, right)

# ---------------------------------------------------------------------------------------
# Quick Sort
# ---------------------------------------------------------------------------------------

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)


def quickSortHelper(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(array, first, last):
   pivotvalue = array[first]
   leftmark = first+1
   rightmark = last

   done = False
   while not done:
       while leftmark <= rightmark and array[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while array[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           array[leftmark], array[rightmark] = array[rightmark], array[leftmark]

   array[first], array[rightmark] = array[rightmark], array[first]
   return rightmark

# ---------------------------------------------------------------------------------------
# Heap Sort
# ---------------------------------------------------------------------------------------
def maxHeapify(array, i, heapSize):
    left  = 2*i+1
    right = 2*i+2
    largest = i

    if(left <= (heapSize-1)) and (array[left] > array[i]):
        largest = left
    if (right <= (heapSize-1)) and (array[right] > array[largest]):
        largest = right

    if i != largest:
        array[i], array[largest] = array[largest], array[i]
        maxHeapify(array, largest, heapSize-1)

def buildMaxHeap(array, heapSize): #ok
    idxs = range(len(array)/2, -1, -1)
    for index in idxs:
        maxHeapify(array, index, heapSize)

def heapSort(array):
    heapSize = len(array)
    buildMaxHeap(array, heapSize)
    idxs = range(len(array)-1, 0, -1)
    for index in idxs:
        array[0], array[index] = array[index], array[0]
        heapSize = heapSize - 1
        maxHeapify(array, 0, heapSize)

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
