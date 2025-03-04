def quick_sort(array):
    if len(array) <= 1:
        return array # This is our base case. An array with 0 or 1 element is already sorted.
    pivot = array[0] # Picking our pivot. This will be the element that we will compare all other elements to.
    lower = [x for x in array[1:] if x <= pivot] # All elements less than or equal to the pivot.
    higher = [x for x in array[1:] if x > pivot] # All elements greater than the pivot.
    return quick_sort(lower) + [pivot] + quick_sort(higher) # Recursively sorting the elements from the array.