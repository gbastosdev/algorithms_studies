from binary_search import binary_search
import random, timeit, math

def test_binary_search():
    '''Testing binary search function using random integer as item and a list with non duplicated random integers.'''
    random_int = random.randint(1,1000)
    random_numbers = sorted(random.sample(range(1, 1000), 128))
    execution_time = timeit.timeit(lambda: binary_search(list=random_numbers, item=random_int), number=1)
    assert execution_time < math.log10(len(random_numbers)) # Asserting that execution time is less then log(n).



