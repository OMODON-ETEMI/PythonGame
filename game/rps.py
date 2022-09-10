import random 
def rps():
    user = input('r for rock, p for paper, s for scissors \n')
    choice = ['r','p','s']
    computer = random.choice(choice)
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        print (f'Hey you won!!!\ncomputer choose {computer} while you picked {user}')
    elif (user == computer ):
            print (f'It is a tie!!!\ncomputer choose {computer} while you picked {user}')
    else:
        print (f'Hey you lost!!!\ncomputer choose {computer} while you picked {user}')
    
rps()