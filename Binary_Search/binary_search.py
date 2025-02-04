def binary_search(list, item):
    low = 0
    high = len(list) - 1 # Referring to top of the list (last item).

    while low <= high:
        middle = (low + high) // 2 # Reaching the middle of the list.
        guess = list[middle]
        if guess == item:
            return middle # If the guess is the given item, return the element.
        if guess > item:
            high = middle - 1 # If the guess is higher then the given item, then set the top of the list as the middle position - 1. 
        else:
            low = middle + 1  #If the guess is lower than the given item, then set the base of the list as the middle position + 1.
    return None 
 