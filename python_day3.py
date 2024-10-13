# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120: 
#     print("You can ride this ride!")
# else:
#     print("You're too short for this ride! Sorry!")

###########################################################################

# number_to_check = int(input("What is the number you would like to check? "))

# if number_to_check % 2 == 0: 
#     print("This number is even!")
# else:
#     print("This number is odd!")

###########################################################################

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120: 
#     print("You can ride this ride!")
#     age = int(input("How old are you? "))
#     if age <= 12:
#         print("Child tickets are $5!")
#         price = 5
#     elif (age >= 12 and age < 18):
#         print("Youth tickets are $7!")
#         price = 7
#     else:
#         print("Adult tickets are $12!")
#         price = 12
    

#     wants_photo = (input("Do you want a photo taken? Y or N? ")).upper()
#     if wants_photo == "Y":
#         print(f"Your total is ${price + 3}.")
#     else:
#         print(f"Your total is ${price}.")


# else:
#     print("You're too short for this ride! Sorry!")

###########################################################################

# print("Welcome to Python Puzza Deliveries!")
# size = input("What size pizza do you want? S, M, or L? ").upper()
# pepperoni = input("Do you want pepperoni on your pizza? Y or N? ").upper()
# extra_cheese = input("Do you want extra cheese? Y or N? ").upper()

# if size == "S":
#     bill = 15
#     if pepperoni == "Y": 
#         bill += 2
#     if extra_cheese == "Y":
#         bill += 1
# elif size == "M":
#     bill = 20
#     if pepperoni == "Y": 
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1
# else: 
#     bill = 25
#     if pepperoni == "Y": 
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1

# print(f"Your total comes out to be ${bill}.")

###########################################################################

print("Welcome to Treasure Island\nYour mission is to find the treasure.")
option_1 = input("You're at a cross road. Where do you want to go?\nType 'Left' or 'Right:'\n").upper()
if option_1 == "LEFT":
    print("You arrived at a lake. There is an island in the middle of the lake.")
    option_2 = input("Will you wait for a boat or will you swin across? Type 'swim' or 'wait:'\n").upper()
    if option_2 == "WAIT": 
        print("A boat arrived and dropped you off in front of three doors.")
        option_3 = input("There is a red, blue and yellow door, which one will you choose? 'Red' or 'Blue' or 'Yellow': \n").upper()
        if option_3 == "YELLOW":
            print("You chose the right door! You found the treasure!")
        elif option_3 == "RED":
            print("As you opened the door, a giant bear claws at you leaving you too injured to move on. GAME OVER!")
        else: 
            print("As you opened the door, a poisonous snake jumped at you and took a big bite. You passed out. GAME OVER!")
    else: 
        print("You realized you don't know how to swim & you drowned. GAME OVER!")
else: 
    print("When you turned right, a bunch of angry clowns started chasing you until you passed out from exhaustion. GAME OVER!")
