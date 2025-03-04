# Explanation
-  Binary Search is basically a algorithm that searches for an occurrence of an item, on a list. 
    - Think on this example: You have to find a name on a agenda and you're using a simple search for it -> O(n). If you're searching for a person called Adit, this is the first person on your list. As this is the best scenario possible, this will be 0(1).
    - Now, if you're serching for Zayan, this will take long time to you reach the final page of the agenda. On Big O notation, this will be O(n), because you had to pass through all of the list.
    - Thinking on time execution, we always aim on having this to run as low as possible. So, implementing a script that will find the item, aiming the best time for it, you'd necessarily create a O(log(n)) script. Translating the 'binary_seach.py' file into few words, we will have:
        - The script, first of all, need a single pre-requisite: *`The list HAS to be sorted`*
        - Create two pointers. One at the beginning (low) and other at the end (high) of the list.
        - Loop while you didn't reach a single item.
        - Find the middle of the list. Obs: Using python, we can do (low + high) // 2. This means that the equation will always be rounded down, if the number is not even.
        - Get the element of that position on the list. This will be your guess!
        - Conditionals:
            - If the guess is equal than the item, so the script found the item.
            - If the guess is higher than the item, so high will receive middle - 1. This means that the script will ignore the middle to the end of the list.
            - If the guess is lower than the item, so low will receive middle + 1. This means that the script will ignore the begginning to the middle of the list.
        - If the script didn't find the given item, will return `None`.
    
