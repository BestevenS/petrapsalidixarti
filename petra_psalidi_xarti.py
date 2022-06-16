import random

#Just changed something for the git

choises = ['Rock', 'Scissors', 'Paper']
score = {'Computer': 0, 'Player': 0}

menu = """1) Rock
2) Scissors
3) Paper
0) To exit """

def show_result(choise, computer_choise):
    if choise == computer_choise:
        print('Draw')
        return

    if choise - computer_choise in [-1, 2]: # Dimitris Android sugestion
        print('You win!')
        score['Player'] += 1
        return
        
    print('You lose!')
    score['Computer'] += 1
    return

    
def show_result_refactored_1(choise, computer_choise):
    if choise == computer_choise:
        print('Draw')
        return

    if (choise - computer_choise) % 3 == 1:
        print('You lose!')
        score['Computer'] += 1
        return

    print('You win!')
    score['Player'] += 1 
    return

def show_result_refactored_2(choise, computer_choise):
    if choise == computer_choise:
        print('Draw')
        return

    if choise - computer_choise == -1 or choise - computer_choise == 2:
        print('You win!')
        score['Player'] += 1 
        return

    print('You lose!')
    score['Computer'] += 1 
    return





while True:
    print(f"The score is: Computer: {score['Computer']} | You: {score['Player']}")
    print(menu)
    choise = int(input('Please select:'))

    if choise not in range(4):
        print('Please select an option between 0-3')
        continue

    if choise == 0:
        break

    choise -= 1
    
    print(f'Your selection was: {choises[choise]}')

    computer_choise = random.randrange(3)
    print(f'Computer selection is: {choises[computer_choise]}')
    # show_result(choise, computer_choise)
    show_result_refactored_2(choise, computer_choise)
    print('-'*80)
