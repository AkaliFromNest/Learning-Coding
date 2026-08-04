# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Create an empty list to store results later
squares = []

# Go through each number "n" in the list, one by one
for n in numbers:

# Take that number, square it (n ** 2), and add it to the "squares" list
    squares.append(n ** 2)

print(squares)
# Show the result: [1, 4, 9, 16, 25]


# Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# For each number "n" in the list, keep it only if it's even (n % 2 == 0)
# Save all the even numbers into a new list called "pairs"
pairs = [n for n in numbers if n % 2 == 0]

print(pairs) # [2, 4, 6, 8, 10]


#Here is an example adding some expression+conditions
numbers = [1, 2, 3, 4, 5, 6]
result = ["even" if n % 2 == 0 else "odd" for n in numbers]

print(result) # ['odd', 'even', 'odd', 'even', 'odd', 'even']