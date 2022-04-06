# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

from sorts import *

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
if __name__ == '__main__':

    array = [54,26,93,17,77,31,44,55,20]

    array1 = list(array)
    array2 = list(array)
    array3 = list(array)
    array4 = list(array)
    array5 = list(array)
    array6 = list(array)
    array7 = list(array)

    print("* Bubble Sort: ")
    print("Antes: ", array1)
    bubbleSort(array1)
    print("Depois:", array1)
    print("\n")

    print("* Short Bubble Sort: ")
    print("Antes: ", array2)
    shortBubbleSort(array2)
    print("Depois:", array2)
    print("\n")

    print("* Selection Sort: ")
    print("Antes: ", array3)
    selectionSort(array3)
    print("Depois:", array3)
    print("\n")

    print("* Insertion Sort: ")
    print("Antes: ", array4)
    insertionSort(array4)
    print("Depois:", array4)
    print("\n")

    print("* MergeSort: ")
    print("Antes: ", array5)
    array5 = mergeSort(array5)
    print("Depois:", array5)
    print("\n")

    print("* Quick Sort: ")
    print("Antes: ", array6)
    quickSort(array6)
    print("Depois:", array6)
    print("\n")

    print("* Heap Sort: ")
    print("Antes: ", array7)
    heapSort(array7)
    print("Depois:", array7)
    print("\n")

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
