# autor: Edimar Chaves Jr.
#30/10/2021 20:04:40:02
# The Three way quicksort it is an optimized version of traditional quicksort
#this one deals better with several occurrences of elements equal to the pivot.

def sort(array, l, r):
    if l < r:
        partition(array, l, r)

def partition(array, l, r):

    if l < r:

        start = l
        end = r
        i = l
        pivot = array[l]

        while i <= end:

            if array[i] < pivot:
                array[start], array[i] = array[i], array[start]
                start += 1
                i += 1
            
            elif array[i] > pivot:
                array[i], array[end] = array[end], array[i]
                end -= 1
            
            else:
                i += 1
        
        sort(array, l, start - 1)
        sort(array, end + 1, r)