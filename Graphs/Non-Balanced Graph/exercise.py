morning_graph = {}
morning_graph['wake_up'] = ['brush_teeth', 'workout', 'wrap_food']
morning_graph['wrap_food'] = []
morning_graph['brush_teeth'] = ['breakfast']
morning_graph['workout'] = ['shower']
morning_graph['shower'] = ['get_dressed']
morning_graph['breakfast'] = []
morning_graph['get_dressed'] = []

# According to "Understanding Algorithms" page 134, section 6.4, the morning routine graph should look like:
# wake_up -> brush_teeth, workout, wrap_food
# brush_teeth -> breakfast
# workout -> shower
# shower -> get_dressed
# wrap_food -> (no outgoing edges)
# breakfast -> (no outgoing edges)
# get_dressed -> (no outgoing edges)

# Your graph is almost correct, but you are missing the 'breakfast' and 'get_dressed' nodes as keys with empty lists.
# Let's add them for completeness:


print("Morning routine graph:", morning_graph)
