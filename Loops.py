# 4.1. Loop with a counter variable
i = 0
while i < 5:
    print("hello")                 # will priont hi 5 times
    i += 1

# --------------
# 4.2. Loop with an accumulator variable
total = 0                         # accumulator
i = 1                             # counter
while i <= 10:
    total += i                    # add to the accumulator
    i += 1                        # increase the counter

# --------------
# 4.3. break
i = 0

while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1

# --------------
#4.4. continue
i = 0

while i <= 10:
    if i == 5 or i == 7:
        i += 1
        continue
    print(i)
    i += 1

# --------------
# 4.5. Get user input in a loop
i = 0                                         # counter
total = 0                                     # accumulator

while i < 5:                                  # set to loop 5 times
    num = int(input("Enter number: "))
    total += num
    i += 1

print(total)

# --------------
# 4.6. Quit loop with sentinel value
total = 0

while True:
    num = int(input("Enter number, -1 to stop: "))
    if num == -1:
        break
    total += num

print(total)

# --------------
# 4.7. Loop through a string (while)
name = "Mr. Gallo"

i = 0
while i < len(name):
    print(i, name[i])
    i += 1

# --------------
# 4.8. Loop through a list (while)
friends = ["Frank", "Sally", "Jimbo"]

i = 0
while i < len(friends):
    print(i, friends[i])
    i += 1

# --------------
# 4.9. Loop through a string (for)
name = "Mr. Gallo"

for character in name:
    print(character)

# --------------
# 4.10. Loop through a list (for)
friend_list = ["Frank", "Sally", "Jimbo"]

# For every friend in my friend list
# print the friend
for friend in friend_list:
    print(friend)

# --------------
# 4.11. Loop using range
# while loop print 50-100
i = 50
while i <= 100:
    print(i)
    i += 1

# range(start, end)... Goes up to, but, doesn't include the end
for num in range(50, 101):
    print(num)


# while loop print 1-25 by 5
i = 0
while i <= 25:
    print(i)
    i += 5

# range(start, end, step)
for num in range(0, 26, 5):
    print(num)

# --------------
# 4.12. Loop using enumerate
name = "Mr. Gallo"

for i, character in enumerate(name):
    print(i, character)

# --------------
# 4.13. String building and filtering
my_string = ""
for n in range(65, 70):
    my_string += str(n) + " "

print(my_string)  # "65 66 67 68 69 "

# --------------

nums = [1, 6, -4, 1, -5, 1]

only_ones = []
for n in nums:
    if n == 1:
        only_ones.append(n)

print(only_ones)  # [1, 1, 1]
