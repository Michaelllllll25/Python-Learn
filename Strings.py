message = "Hello"         # String
message2 = 2              # Not a string

print("Hello world")
print(message)

print("#########################")

a = """Bobby and the people
went into the shop to buy a         
pair of Jordan 1 Low's"""
print(a)

print("#########################")

b = "Hello World"
print(len(b))          # Counts length of words
print(b[0])            # Prints first character (H)
print(b[1])            # Prints second character (e)
print(b[0:5])          # Prints first charcter up to but not including the fith (Hello)
print(b[6:])           # Prints "World"
#                                         ^^^^^^^Slicing

print("#########################")

c = "Hello World"
print(c.lower())             # Prnts string in lower case
print(c.upper())             # Prnts string in upper case
print(c.count('o'))          # Counts number of characters in the string
print(c.find('World'))       # Finds the word in the string, will return the index where the character can be found (worlds starts at 6th character)

print("#########################")

d = "Hello World"
new_d = d.replace('World', 'Universe')  # Used to replace 
print(new_d)

print("#########################")

greeting = "Hello"
name = "Michael"
                                    
e = greeting + ', ' + name + '. Welcome!'       # Concatination
print(e)

print("#########################")

greeting1 = "Hello"
name1 = "Michael"                             

f = '{}, {}. Welcome!'.format(greeting1, name)    # Format words into same sentence
print(f) 

g = f'{greeting}, {name.upper()}. Welcome!'               # Formating using f-string
print(g)                           

print("#########################")
