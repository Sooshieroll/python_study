# Strings
# print("123" + "456") would print out 123456 instead of adding

# Integers
# print(123 + 456) would actually add

# Floats
# numbers with decimals

# Booleans
# True or False

# print(type("Hello"))
# print(type(123))
# print(type(123.45))
# print(type(True))

# name_of_user = input('Enter your name:\n')
# length_of_name = len(name_of_user)

# print("Number of letters in your name: " + str(length_of_name))

# weight = 84
# height = 1.65

# bmi = weight / (height**2)
# print(bmi)
# print(round(bmi)) # 31
# print(round(bmi, 2)) # 30.85

print("Welcome to the Tip Calculator!")
bill_amount = float(input("what was the total of the bill?\n$"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill with?\n"))

bill_with_tip = bill_amount * (1 + tip_percentage / 100)
total = bill_with_tip = bill_with_tip / people
final_amount = round(total, 2)

print(f"The total cost per person is: ${final_amount}")


# print(type(bill_amount))
# print(type(tip_percentage))
# print(type(people))
# print(type(total))


