#------------------------------
# ABOUT PYTHON SEQUENCES
#------------------------------

# A Python sequence is an ordered group of things
# There are several types of sequences
# (e.g., lists, tuples, strings, ranges, and others)

#----- ALL PYTHON SEQUENCES ARE ITERABLE -----

# For <element> in <sequence>
    # FOR (each element)
    # IN (a sequence)
    # LOOP (do this action)

my_name = "James"

for letter in my_name:
    print(letter)

groceries = ['roast beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog']

for item in groceries:
    print(item)

# <hr>
print("\n" + "-" *20)

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

# <hr>
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

# <hr>
print("\n" + "-" *20)

#------------------------------
# ITERATING WITH RANGES
#------------------------------

# Range [start, stop, step]

for i in range(1, 10):
    if i == 9:
        print(i)
    else:
        print(i, end=", ")
    
# <hr>
print("\n" + "-" *20)

#------------------------------
# SEQUENCES OPERATIONS
#------------------------------

#----- SLICING -----

# Var[start:stop:step]

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

print(rainbow[3:])
print(rainbow[::2])
print(rainbow[::-1])
print()

#----- LEN, MIN, MAX -----

nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(nums))
print(max(nums))
print(min(nums))
print()

my_string = 'treehouse'
print(len(my_string)) # Len returns total letters in the string
print(max(my_string)) # Max returns 'u' because its closest to z ...
print(min(my_string)) # Min returns the last letter in our string
print()

# What happens if we have a string with numbers in it?
    # Python uses "lexigraphical ordering"
    # (strings that are numbers to be smaller than strings that are letters)
mixed = 'treehouse2020'
print(len(mixed))
print(max(mixed))
print(min(mixed))

# <hr>
print("\n" + "-" *20)

#----- MEMBERSHIP TESTING -----

# A method is just a function 
# Determine if an item or sequence is INSIDE another sequence

docs = 'We saw that lists and strings have many common properties, such as indexing and slicing operations. They are two examples of sequence data types (see Sequence Types — list, tuple, range). Since Python is an evolving language, other sequence data types may be added. There is also another standard sequence data type: the tuple.'

# Check if 'tuple' is in the paragraph
if 'tuple' in docs:
    print('tuple is here!')
else:
    print('tuple is not here...')

# Check if 'tuple' is NOT in the paragraph
if 'tuple' not in docs:
    print('tuple is not here...')
else:
    print('tuple is here!')
print()

#----- COUNT AND INDEX -----

# We can also use methods to determine how many times a given object appears in a sequence
    # A method is just a function that is called on a specific object!!!
    # Sequences are objects, and they have special methods that can be called on them

# How many time does the string tuple occurs in docs (not exact matches only)
print(docs.count('tuple'))

# Find the index of the first occurence of an object inside a sequence
print(docs.index('tuple'), '\n')

# Find the index where 'Nicole' appears in the list
teachers = ['Alena', 'Ashley', 'Nicole', 'Treasure', 'Ralph', 'Nicole']
print(teachers.index('Nicole'))
print(teachers.count('Nicole'))

# <hr>
print("\n" + "-" *20)

#------------------------------
# CONCATENATION AND MULTIPLICATION
#------------------------------

# Attach one object to the end of another (mutable sequences)
# For immutable sequence types, concatenation always involves creating a new object
# This is not memory efficient (consider a different data structure vs. immutable ...)

object1 = [1, 2, 3, 4, 5,]
object2 = [6, 7, 8, 9, 10]

object1 = object1 + object2
print(object1)

#----- MULTIPLICATION -----

# Concatenation multiple times - Also called "repitition"
str = 'python'
print((str + ", ") *5)

