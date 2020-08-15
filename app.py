#------------------------------
# ABOUT PYTHON SEQUENCES
#------------------------------

# A Python sequence is an ordered group of things
# There are several types of sequences
# (e.g., lists, tuples, strings, ranges, and others)

#----- ALL PYTHON SEQUENCES ARE ITERABLE -----

# FOR (each element)
# IN (a sequence)
# LOOP (do this action)

# For <element> in <sequence>
my_name = "James"

for letter in my_name:
    print(letter)

# Iterate through a groceries list
groceries = ['roast beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog']

for item in groceries:
    print(item)


#------------------------------
# THE ENUMERATE FUNCTION
#------------------------------

# Manually enumerate via a counter (and f string)

index = 1

# Use an 'f string' - lets us print variables inside of strings (Python 3 only)
for item in groceries:
    # Type the letter f before your string
    # Then, put your variable in your string surrounded by curly braces {}
    print(f'{index}: {item}')
    index += 1

# TERMINAL SPACING ...
print("\n" + "-" *20)

#----- ENUMERATE FUNCTION IS MORE EFFICIENT -----

# Returns an 'enumerate object'
    # Replaces the reference to the groceries list with a call to the enumerate function
    # where we pass the groceries list as an argument to it ...

# Use multiple assignment
    # The optional argument '1' tells us to start counting at 1 instead of 0
    # Note, the optional argument will take any valid integer (where we want to start counting)
for counter, item in enumerate(groceries, 1):
    print(f'{counter}: {item}')


#------------------------------
# ITERATING WITH RANGES
#------------------------------











