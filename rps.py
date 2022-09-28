from multiprocessing.resource_sharer import stop
import random
from timeit import repeat
a = ['rock', 'paper', 'scissors']

while(True):
   human_turn = input('Enter your turn or type exit:')
   computer_turn = random.choice(a)
   if human_turn == 'exit':
      print('See you!')
      break

   print(f'Human:{human_turn} vs. Computer:{computer_turn}')

   if human_turn == computer_turn:
      print ("Draw")
   elif human_turn == 'rock' and computer_turn == 'scissors':
      print ('Human Wins!')
   elif human_turn == 'paper' and computer_turn == 'rock':
      print ('Human Wins!')
   elif human_turn == 'scissors' and computer_turn == 'paper':
      print ('Human Wins!')
   else:
      print('Computer Wins!')
