from collections import deque
jet_to_cow = {}
jet_to_cow['jet'] = ['tat','cat']
jet_to_cow['tat'] = ['cat', 'mad']
jet_to_cow['cat'] = ['rat', 'cow']
jet_to_cow['mad'] = ['cow']
jet_to_cow['rat'] = ['cow']

def found_cow(name:str) -> bool:
    return name == 'cow'  # Example condition to check if a person is a cow. This simple matches names ending with 'cow'.

def search(name) -> bool:
    search_queue = deque()
    search_queue += jet_to_cow[name]
    verified = []  # This list is used to keep track of the people we have already visited.
    while search_queue:
        person = search_queue.popleft()
        print("Visiting:", person)
        if person not in verified:
            if found_cow(person):
                print("Found cow: {0}", person)
                return True
            else:
                search_queue += jet_to_cow[person]# If condition is not met, add the next people to the queue.
                verified.append(person)  # Mark the person as verified to avoid revisiting.
    print("No cow found in the graph.")
    return False
search('jet')  # Call the search function using 'jet' as the starting point.