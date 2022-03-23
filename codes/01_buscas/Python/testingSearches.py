# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

from searches import *

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

if __name__ == '__main__':

    unorderedList = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    orderedList = [0, 1, 2, 8, 13, 17, 19, 32, 42]

    print("* Sequential Search")
    print(sequentialSearch(unorderedList, 3))
    print(sequentialSearch(orderedList, 13))

    print("* Ordered Search")
    print(orderedSearch(unorderedList, 3))
    print(orderedSearch(orderedList, 13))

    print("* Binary Search")
    print(binarySearch(unorderedList, 3))
    print(binarySearch(orderedList, 13))

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
