# ---------------------------------------------------------------------------------------
# Sequential Search
# ---------------------------------------------------------------------------------------

def sequentialSearch(array, item):
    pos = 0
    found = False
    while pos < len(array) and not found:
	       if array[pos] == item:
	              found = True
	       else:
	              pos = pos+1
    return found

# ---------------------------------------------------------------------------------------
# Ordered Search
# ---------------------------------------------------------------------------------------

def orderedSearch(array, item):
    if sorted(array) != array:
        print("Array is not sorted!")
        return False

    for i in range(len(array)):
        if item == array[i]:
            return True
        if array[i] > item:
            return False

    return False

# ---------------------------------------------------------------------------------------
# Binary Search
# ---------------------------------------------------------------------------------------

def binarySearch(array, item):

    found = False
    if sorted(array) != array:
        print("Array is not sorted!")
        return found

    first = 0
    last = len(array)-1

    while first<=last and not found:
        midpoint = (first + last)//2
        if array[midpoint] == item:
            found = True
        else:
            if item < array[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
