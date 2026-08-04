#Here as you can see we have the variable called word and the value is Python
#So what the string do is to have access to the charactersÇ


#1.Indexing
word = "Python"
print(word[0])   # P (The first character, the index start at 0)
print(word[1])   # y
print(word[-1])  # n (Index negative = For the end)
print(word[-2])  # o

#2.Slicing
word = "Python"
print(word[0:2])   # "Py"  (From the index 0 to 2, without including the 2)
print(word[2:])    # "thon" (From the index 2 to the final)
print(word[:3])    # "Pyt"  (from the beginning to the index 3)
print(word[::-1])  # "nohtyP" (the string backwards — a very used trick)

# This is the Syntax string[start:end:step]


#3. Most commonly used methods
#Here we have the varibale with the value
text = "Hello World"
#We print it but if you see whe have the variable with a .parameter that change the syntax
print(text.strip()) # "Hello World" — removes leading/trailing spaces
print(text.lower()) # "hello world" — all lowercase
print(text.upper()) # "HELLO WORLD" — all uppercase
print(text.replace("Hello", "Goodbye")) # replaces text
print(len(text)) # length of string (includes spaces)
print("Hello" in text) # True — checks if something is contained


#4. Splitting and joining strings
#Here the same.
phrase = "Python is great"
words = phrase.split(" ") # ['Python', 'is', 'great'] → splits it into a list
print(words)

list = ["Python", "is", "great"]
joined = " ".join(list) # "Python is great" → joins it again
print(joined)


#-------------------------------------------------------------------------------------------------------------------------------
#This is an example
phrase = "Python is a very versatile language"

# 1. Count words
# 2. Display in reverse
# 3. Display in uppercase
# 4. Replace "versatile" with "powerful"

Count = print(phrase.split(""))
print(len(Count))
print(phrase[::-1])
print(phrase.upper())
print(phrase.replace("versatile", "powerful"))

