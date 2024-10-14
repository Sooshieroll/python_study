import random

# random_integer = random.randint(1, 10) ## will give a number from 1-10 (including 1 and 10)
# print(random_integer)

# random_number = random.random() ## floating number between 0 and 1 (not including 1)
# print(random_number)

# random_float = random.uniform(1, 10) ## floating number between 1 and 10 (including 1 and 10) 
# print(random_float)

# random_integer = random.randint(0,1)
# print(random_integer)
# if random_integer == 0:
#      print("Heads")
# else: 
#      print("Tails")

###########################################################################

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# states_of_america.extend(["Lucy land", "Steele Land"])
# print(states_of_america)

###########################################################################

# friends = ["Lucy", "Jake", "Efrying", "Epik", "Andres"]

# # random_index = random.randint(0,4)
# # print(friends[random_index])

# choice = random.choice(friends)
# print(f"{choice} has to pay the bill!")

###########################################################################

# print(len(states_of_america))
# num_of_states = len(states_of_america)
# print(states_of_america[num_of_states -1])

# dirty_dozen = ["Strawberries", "Peaches", "Nectarines", "Apples", "Grapes", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes", "Spinach", "Kale"]
# fruits = ["Strawberries", "Peaches", "Nectarines", "Apples", "Grapes", "Cherries", "Pears", "Tomatoes"]
# vegetables = ["Celery", "Potatoes", "Spinach", "Kale"]

# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)

###########################################################################

choices = ["Rock", "Paper", "Scissors"]
user_hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors\n"))
# if user_hand == 0:
#     print("You chose Rock.")
# elif user_hand == 1:
#     print("You chose Paper.")
# elif user_hand == 2: 
#     print("You chose Scissors.")

computer_hand = random.randint(0,2)
print("You chose:")
print(choices[user_hand])
print("Computer chose:")
print(choices[computer_hand])


# if computer_hand == 0:
#     print("Computer chose Rock.")
# elif computer_hand == 1:
#     print("Computer chose Paper.")
# elif computer_hand == 2: 
#     print("Computer chose Scissors.")

# print(f"Computer chose {computer_hand}.")
if user_hand >= 3 or user_hand < 0:
    print("You typed an invalid number, try again and choose between 0 and 2")
elif user_hand == computer_hand:
    print("It's a Draw! Try again!")
elif user_hand == 0 and computer_hand == 2: 
    print("You win!")
elif computer_hand == 0 and user_hand == 2:
    print("You lose!")
elif computer_hand > user_hand:
    print("You lose!")
elif user_hand > computer_hand:
    print("You win!")


