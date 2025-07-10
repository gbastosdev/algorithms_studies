from collections import deque
graph = {}
graph['me'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggym']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []


# This is a simple breadth-first search algorithm to find a person in a graph.
# It uses a queue to explore each person and their connections until it finds the target person or exhausts the search.

def is_person_seller(name: str) -> bool:
    return name[-1] == 'm' # Example condition to check if a person is a seller. This simple matches names ending with 'm'.

def search(name) -> bool:
    search_queue = deque()
    search_queue += graph[name]
    verified = [] # This list is used to keep track of the people we have already visited.
    while search_queue:
        person = search_queue.popleft()
        if person not in verified:
            print("Visiting:", person)
            if is_person_seller(person):
                print("Found mango seller:", person)
                return True
            else:
                search_queue += graph[person] # If condition is not met, add the next people to the queue.
                verified.append(person) # Mark the person as verified to avoid revisiting.
    print("No mango seller found in the graph.")
    return False
print(search('me')) # Call the search function using 'me' as the starting point.