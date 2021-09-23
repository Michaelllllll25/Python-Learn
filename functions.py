def hello_func():
    print("Hello Function!")

hello_func()                  # need this line to run the code

# --------------

def hello(greeting, name):
    return f"{greeting} {name} "

print(hello('greeting', name = 'mike'))

# --------------

name = input("Name: ")
age = input("Age: ")
def name_age(name: str, age: int) -> str:
    return name + age

print(name_age(name, age))
# or
result = name_age(name, age)
print(result)

# --------------

num_1 = int(input("Num1: "))
num_2 = int(input("Num2: "))

def average(num_1: int, num_2: int) -> float:
    return (num_1 + num_2) / 2

print(average(num_1, num_2))

# --------------

num_1 = int(input("Num 1: "))
num_2 = int(input("Num 2: "))
num_3 = int(input("Num 3: "))

def largest(num_1, num_2, num_3):
    if (num_1 > num_2) and (num_1 > num_3):
        largest_num = num_1
    elif (num_2 > num_1) and (num_2 > num_3):
        largest_num = num_1
    else:
        largest_num = num_3

    print("The largest number is ", num_1)

largest(num_1, num_2, num_3)
