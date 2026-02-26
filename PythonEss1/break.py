# # break - example

# print("The break instruction:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Inside the loop.", i)
# print("Outside the loop.")


# # continue - example

# print("\nThe continue instruction:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Inside the loop.", i)
# print("Outside the loop.")


# secret_word = "chupacabra"
# while True:
    # word = input("Enter the secret word ")
    # if word == secret_word:
        # print ("You've successfully left the loop.")
        # break

counter = 5

secret_word = "chupacabra"
while counter > 0:
    word = input("Enter the secret word ")
    if word == secret_word:
        print ("You've successfully left the loop.")
        break
    counter -= 1
