# hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# # Step 1: write a line of code that prompts the user
# number = input("Enter a numbber: ")
# # to replace the middle number with an integer number entered by the user.
# hat_list[2] = number

# # Step 2: write a line of code that removes the last element from the list.
# del hat_list[4]

# # Step 3: write a line of code that prints the length of the existing list.
# print("lenth:",len(hat_list))

# print(hat_list)

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

my_list = ["white", "purple", "blue", "yellow", "green"]

for color in my_list:
    print(color)




