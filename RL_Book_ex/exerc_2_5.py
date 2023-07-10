"""Exercise 2.5 (programming) Design and conduct an experiment to demonstrate
 difficulties that sample-average methods  have for problems. Use a modified
version of the 10-armed testbed in which all the q⇤(a) start out equal and 
then take independent random walks (say by adding a normally distributed 
increment with mean 0 and standard deviation 0.01 to all the q⇤(a) on 
each step).
 Prepare plots like Figure 2.2 for an action-value method using 
sample averages, incrementally computed, and another action-value method 
using a constant step-size parameter, ↵ = 0.1. Use " = 0.1 and longer runs,
say of 10,000 steps """

import matplotlib.pyplot as plt
import numpy as np
from numpy import random
from scipy.stats import norm

class kArmedThug:
    def __init__(self):
        self.k = 10
        self.distr_means = {i:0 for i in range(self.k)}

    def sample(self, action):
        return random.normal(loc = self.distr_means[action])
    
    def updateDistributions(self):
        #print("updated distr_means")
        for key, value  in self.distr_means.items():
            self.distr_means[key] += (random.normal(loc = 0, scale = 0.01))
            
    def showDistributions(self):
        #print("Current Distribution Means are: ")
        print(self.distr_means)
             
    def plotDistributionsForActions(self,actions = [i for i in range(0,10)]):
        """ Plot Normal Distribution of a list of Actions """
        x_axis = np.arange(-7,7,1e-3)
        plt.title("Probability Distibutions of the k = "+ str(self.k)+
                  " Levers")
    
        if( len(actions) > 0 & len(actions) <= self.k):
            for a in actions:
                y_axis = norm.pdf( x_axis, self.distr_means[a])
                plt.plot(x_axis, y_axis, label = "Action " + str(a)) 
        else:
            pass
        plt.legend()
        plt.show()
        
#------------------------------------------------------


class kSolver:
    def __init__(self):
        self.k = 10
        self.estimates = {action:0 for action in range(self.k)}
        self.tries = {action:0 for action in range(self.k)}
        self.total_reward = 0
        print("Initializing a Cadet hunting for kArmedThugs.")
    
    def averageReward(self):
        return self.total_reward / sum(self.tries.values())

class kPoliceman(kSolver):
    def chooseAction(self):
        eps = 0.1
        if (random.rand() < eps):
            return random.randint(0,self.k)
        else:
            values = list(self.estimates.values())
            return np.argmax(values)
        


    def learningStep(self, thug):
        action = self.chooseAction()
        reward = thug.sample(action)
        self.tries[action] += 1
        self.estimates[action] +=  (1 / self.tries[action] * (reward - self.estimates[action]))
        self.total_reward += reward
        return reward

    def train( self ,steps,  thug, nonstationary = False):
        history = []
        for i in range(steps):
            self.learningStep(thug)
            history.append(self.averageReward())
    
            if(nonstationary):
                thug.updateDistributions()

        return history
class kDetective(kPoliceman):
    def __init__(self):
        super().__init__()
        self.stepsize = 0.1
    def learningStep(self, thug):
        action = self.chooseAction()
        reward = thug.sample(action)
        self.tries[action] += 1
        self.estimates[action] +=  (self.stepsize * (reward - self.estimates[action]))
        self.total_reward += reward
    
        return reward
class kSpecialAgent(kDetective):
    def learningStep( self, thug):
        super().learningStep(thug)
        self.stepsize -= 1e-3



#---------------------------------------------------------------

STEPS = 10000

thug = kArmedThug()

for i in range(10000):
    #thug.updateDistributions()
    pass




def plot_averageReward(averageRewardsHistorys, labels):
    for idx, history in enumerate(averageRewardsHistorys):
        x_axis = np.arange(0,len(history),1)
        y_axis = history
        plt.plot(x_axis,y_axis, label = labels[idx])
    plt.title("Performance of models")
    plt.xlabel ("Steps")
    plt.ylabel ("Average Reward")
    plt.legend()
    plt.show()


police = []
histories = []
labels = ["Policeofficer Sample Average Smith",
          "Detective Constante Stepsize",
          "Special Agent Small Decrease"]
police.append(kPoliceman())
police.append(kDetective())
police.append(kPoliceman())
for cadet in police:
    histories.append(cadet.train(STEPS, thug, nonstationary = True))
#thug.plotDistributionsForActions()   
plot_averageReward(histories, labels)
print("-"*100)
print("The Distributions Means MAXIMUM is: ")
print(max(thug.distr_means.values()))
"""To Do
 - visualization in form of a learning graph
 - program 2 more law inforcement algorithms
   - one with incrementally decreased stepsize 
   - one with constant stepsize

"""
