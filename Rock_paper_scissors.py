import random

print('===========================')
print(' Rock✊ Paper✋ Scissors✌️')
print('===========================')

print(' 1) ✊')
print(' 2) ✋')
print(' 3) ✌️')

player = int(input('Enter a number between 1&3: '))
computer = random.randint(1,3)

print(f'You chose {player}')
print(f'Computer chose {computer}')

if computer == player:
    print("It's a tie!")
elif (player == 1 and computer == 3) or ( player == 2 and computer == 1) or ( player == 3 and computer == 2):
    print('You win! 🎉')
else:
    print('Computer wins! 🤖')
