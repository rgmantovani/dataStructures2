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
    letf_index  = 0
    right_index = 0
    result = []

    while left_index < len(left) and right_index < len(right):
        if(left[left_index] < right[right_index]):
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def mergeSort(array):

    print("Merge Sort")
    print(array)

    #ending the recursion (base criteria)
    if len(array) <= 1:
        return array;

    # divide the array in half, call recursions, and merge halves
    half     = len(array)//2
    left     = mergeSort(array=array[:half])
    right    = mergeSort(array=array[:half])
    newArray = merge(left=left, right=right)
    return newArray

# ---------------------------------------------------------------------------------------
# Quick Sort
# ---------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
