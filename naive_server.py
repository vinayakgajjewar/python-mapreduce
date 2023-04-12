from collections import defaultdict

# Naive MapReduce implementation
def map_reduce_ultra_naive(input, mapper, reducer):

    # Execute map stage
    map_results = map(mapper, input)

    # Perform shuffle operation to group by key
    shuffler = defaultdict(list)
    for key, value in map_results:
        shuffler[key].append(value)
    
    # Execute reduce stage
    return map(reducer, shuffler.items())

# User code from this point onward

# Input data
words = "yadda yadda yadda beep boop blop ding dong boop beep bop".split(" ")

# Define mapper and reducer functions
mapper = lambda word: (word, 1)
reducer = lambda emitted: (emitted[0], sum(emitted[1]))

# Print results
print(list(map_reduce_ultra_naive(words, mapper, reducer)))