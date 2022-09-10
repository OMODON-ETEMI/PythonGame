# a game that allows the user guess the correct number
# importing random to enable the computer guess a number 
import random 
def guess(x):
# randit is a module under random that enables a range of 1 to the
# defined variable x to be selected at random
    random_number = random.randint(1,x)
    my_number = 0
    while my_number != random_number:
        my_number = int(input(f'Guess a number between 1 - {x}: \n'))
        if my_number > random_number:
            print(f'Ops your {my_number} is too high!!')
        elif my_number < random_number:
            print(f'Ops your {my_number} is too low!!')
            
    print('Yay!! you guessed correctly')
# calling the function
guess (10)
# *this part of the programme is to make the computer guess a
#  number and we give it a feedback if its high or low *
def trial(f):
    low = 0
    high = f
    my_choice = ''
    computer_choice = 0
    while my_choice != 'C':
        computer_choice = random.randint(low, high)
        my_choice = str(input(f'If {computer_choice} is correct type C if it was too high \
type H if it was too low L: ')).upper()
        if my_choice == 'H':
            print (f'Ops {computer_choice} is high ')
            high = computer_choice - 1
        elif my_choice == 'L':
            print(f'Ops {computer_choice} is low')
            low = computer_choice + 1
            
    print(f'Yay!! {computer_choice} is correct')
trial(1000)




