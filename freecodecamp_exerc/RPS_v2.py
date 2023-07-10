import numpy as np
import random
import RPS_game #else no interaction with environment
#------------------------------TODO----------------------------------------
# I dont understand why no work. Maybe the hyperparameters adapt wrong? I should watch freeCodeCampCourse again I think. Or maybe do the other exercise first? Also i dont understand how my model could beat other models that rely on a lot of the past. on the other hand if i put in a lot of input parameters as states it may require a NN
#--------------------------------Hyperparameters--------------------------------------
numberOfStates = 3
numberOfActions = 3
statesList = ["R", "P", "S"]
winningDict = {"R":"S", "S":"P", "P":"R"} #sth beats : sth
Q = np.zeros((numberOfStates ,numberOfActions), dtype = np.double)
lastaction = 0
counter = 0
# initialize Q
#Q[2][0] = 1
#Q[0][1] = 1
#Q[1][2] = 1
  

EPSILON = 0.9 # exploitation grade
ALPHA = 1 #learning rate
GAMMA = 1 #discount of future rewards

#--------------------------------------------------------------------
def rockplayer(prev_play):
  return "R"
def printQ():
  print(Q.round(2))
def getNextState(action):
  return statesList.index(RPS_game.quincy(statesList[action]))
  
def getReward(action, last_action): #unfortunatrely I have to simulate the interaction part
  opponentplay = RPS_game.quincy(statesList[last_action])
  meplay = statesList[action]
  #print("opplay = ", opponentplay, " meplay = ", meplay)
  if(winningDict.get(meplay) == opponentplay):
    result = 1
  elif(meplay == opponentplay):
    result = 0
  else:
    result = -1
  #print("reward is", result)
  return result


def player(prev_play):
  global Q, lastaction, EPSILON, counter, ALPHA
  counter+= 1
  #EPSILON = (1-EPSILON)
  #EPSILON /= 1.01 
  #EPSILON += 0.01
  #EPSILON = (1-EPSILON)
  if(ALPHA>0.0003):
    ALPHA-=0.0003
  #print("alpha = ", ALPHA)
  if(counter % 10 == 0):
    print(Q.round(2))
  if prev_play == '':
    prev_play = 'R'
  
  #     / 0 , 1 , 0 \
  #Q = |  0 , 0 , 1  |
  #     \ 1 , 0 , 0 /
  
  #update q-table:
  state = statesList.index(prev_play) # state (as integer)
  action = np.argmax(Q[state][:]) #optimal action (as integer)
  reward = getReward(action, lastaction)
  nextstate  = getNextState(action)
  Q[state,action] += ALPHA * (reward + GAMMA * max(Q[nextstate]) - Q[state,action] )
  
  guess = statesList[action] #choose action noted in Q-table

  
  #return a random or q-table answer
  if(random.random() > EPSILON):
    guess = random.sample(statesList,1)[0]
  else:
    guess
  lastaction = statesList.index(guess)
  return guess
  