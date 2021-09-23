######################################### 5.1. Creating a list
empty_list = []
empty_list
#[]
another_empty_list = list()
another_empty_list
#[]
odd_nums = [1, 3, 5, 7, 9]
odd_nums
#[1, 3, 5, 7, 9]
my_friends = ["Jim", "Joe", "Sally"]
my_friends
#['Jim', 'Joe', 'Sally']
vowels = ['a', 'e', 'i', 'o', 'u']
vowels
#['a', 'e', 'i', 'o', 'u']
vowels = list("aeiou")
vowels
#['a', 'e', 'i', 'o', 'u']
letters = list("hello")
letters
#['h', 'e', 'l', 'l', 'o']
friends = "Jim Sally Joe".split(" ")
friends
#['Jim', 'Sally', 'Joe']
friends = "Jim, Sally, Joe".split(", ")
friends
#['Jim', 'Sally', 'Joe']

######################################### 5.2. Accessing list elements
marks =  [6, 2, 8, 5, 0, 4, 1]                    # Initalizing a list
marks[0]                                          # Access single element by index
#6
marks[3]
#5

######################################### 5.3. Slicing a list
marks =  [6, 2, 8, 5, 0, 4, 1]
marks[3:5]                       # Slice list from index 3 up to (not including) 5
#[5, 0]
marks[:5]                        # Slice list from beginning up to (not including) 5
#[6, 2, 8, 5, 0]
marks[3:]                        # Slice list from 3 to the end
#[5, 0, 4, 1]
marks[:-1]                       # Slice list from beginning to (not including) the last element
#[6, 2, 8, 5, 0, 4]
marks[:]                         # Slice from beginning to the end (copy whole list)
#[6, 2, 8, 5, 0, 4, 1]
marks[::2]                       # Slice from beginning to the end stepping by 2
#[6, 8, 0, 1]
marks[::-1]                      # Slice from beginning to the end backwards
#[1, 4, 0, 5, 8, 2, 6]

######################################### 5.4. Appending elements to a list
friends = ['Jim', 'Sally', 'Lucy']
friends.append("ABC")
friends
#['Jim', 'Sally', 'Lucy', 'ABC']
friends.append("Bob")
friends
#['Jim', 'Sally', 'Lucy', 'ABC', 'Bob']

######################################### 5.5. Reassign element at list index
friends = ['Jim', 'Sally', 'Lucy', 'ABC', 'Bob']
friends[2] = "Abigail"
friends
#['Jim', 'Sally', 'Abigail', 'ABC', 'Bob']

######################################### 5.6. Remove list element using .remove
friends = ['Jim', 'Sally', 'Lucy', 'ABC', 'Bob']
friends.remove("Lucy")
friends
#['Jim', 'Sally', 'ABC', 'Bob']

######################################### 5.7. Remove list element at index using del
friends = ['Jim', 'Sally', 'ABC', 'Bob']
del friends[2]
friends
#['Jim', 'Sally', 'Bob']
