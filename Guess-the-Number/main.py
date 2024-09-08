import random 
num = random.randint(0,100)
guess = None
count = 0

while guess!= num:
  guess = int(input('Guess a number: '))
  if guess>num:
    print('The number you guessed is greater')
    count += 1 

  elif guess<num:
    print('The number you guessed is less than the number')
    count += 1 

  else:
    print('winner')
    count += 1
    print(f'It took you {count} guesses!')
    break
