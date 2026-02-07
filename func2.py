# import time
# def happy_new_year(wishes = True):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return

#     time.sleep(1)
#     print("Happy New Year!")
# happy_new_year()

# value = None
# if value is None:
#     print("Sorry, you don't carry any value")


# def strange_function(n):
#     if(n % 2 == 0):
#         return True
#     print(strange_function(2))
# print(strange_function(1))




def is_year_leap(year):
    #
    # Write your code here.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987, 2026]
test_results = [False, True, True, False, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
