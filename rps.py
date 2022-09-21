human_turn = input('What will you choose?')
human_turn_2 = input('What will you choose?')

if human_turn == human_turn_2:
    print ("Draw")
elif human_turn == 'rock' and human_turn_2 == 'scissors':
   print ('Player 1 Wins!')
elif human_turn == 'paper' and human_turn_2 == 'rock':
   print ('Player 1 Wins!')
elif human_turn == 'scissors' and human_turn_2 == 'paper':
   print ('Player 1 Wins!')
else:
    print('Player 2 Wins!')
