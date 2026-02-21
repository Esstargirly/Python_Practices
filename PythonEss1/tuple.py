# # tuple_1 = (1, 2, 4, 8)
# # tuple_2 = 1., .5, .25, .125

# # print(tuple_1)
# # print(tuple_2)

# # var = 123

# # t1 = (1, )
# # t2 = (2, )
# # t3 = (3, var)

# # t1, t2, t3 = t2, t3, t1

# # print(t1, t2, t3)

# # dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# # phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
# # empty_dictionary = {}

# # print(len (dictionary))
# # print(phone_numbers)
# # print(empty_dictionary)

# school_class = {}

# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break
    
#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
# 	    break
    
#     if name in school_class:
#         school_class[name] += (score,)
    
#     else:
#         school_class[name] = (score,)
        
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)

try:
    value = input("Enter a value: ")
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")
