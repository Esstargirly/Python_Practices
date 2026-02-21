secret_number = 87

number = int(input("Enter the sercret number "))

while number != secret_number:
   # print("Ha Ha, you're stuck inmy loop")

   if number == secret_number:
      print("you're out of the loop")

   else:
      print("Ha Ha, you're stuck inmy loop")

      number = int(input("Enter the sercret number"))

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

