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
# ---------------------------------------------------------------------------------------
