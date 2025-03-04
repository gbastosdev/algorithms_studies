from quick_sort import quick_sort
import random

def test_quick_sort():
    '''Testing quick sort function using a list random integers.'''
    random_numbers = random.sample(range(1, 1000), 20)
    sorted_arr = quick_sort(random_numbers)
    assert sorted_arr == sorted(random_numbers) # Asserting that the sorted array is equal to the sorted random numbers.
     
