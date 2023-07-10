# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import numpy as np
numberOfStates = 3
numberOfActions = 3
statesList = ["R", "P", "S"]
Q = np.zeros((numberOfStates ,numberOfActions), dtype = np.double)

# def player(prev_play, opponent_history=[]):
#    opponent_history.append(prev_play)
#
#    guess = "R"
#    if len(opponent_history) > 2:
#        guess = opponent_history[-2]
#
#    return guess

def player(prev_play , opponent_history = []):

  #     / 1 , 0 , 0 \
  #Q = |  1 , 0 , 1  |
  #     \ 0, -1 , 1 /
  # Q table works. Optimization is coming soon...
  Q[2][0] = 1
  Q[0][1] = 1
  Q[1][2] = 1
  if prev_play == '':
    prev_play = 'R'
  guess = statesList[np.argmax(Q[statesList.index(prev_play)])]
  #print( "PPPPPP = ", prev_play)
  #return prev_play
  return guess
  