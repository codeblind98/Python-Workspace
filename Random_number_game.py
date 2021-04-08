import random
number_to_guess = random.randint(1,10)
guess = int(input('Please guess a number between 1 and 10: '))
count_number_of_tries=1
while number_to_guess != guess:
    print('Sorry wrong number')
    
    if guess < number_to_guess:
        print('you guess is less than actual number')
    else:
        print('you guess is greater than actual number')
    
    if count_number_of_tries == 4:
        break
    guess = int(input('Please guess again: '))
    count_number_of_tries += 1

if number_to_guess == guess:
 print('Well done you won!')
 print('You took', count_number_of_tries , 'goes to complete the game')
else:
 print("Sorry - you loose")
 print('The number you needed to guess was', number_to_guess)
print('Game Over')
'''else:
    print('Your guess is right , it is ',number_to_guess) 
if count_number_of_tries==4:
    print('you are out of maximum number of tries')'''  