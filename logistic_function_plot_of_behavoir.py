import sys

import matplotlib.pyplot as plt

sys.setrecursionlimit(1500) # this sets the maximum amount of iterations before an error is called.

def logistic(x,constant):

    x2 = constant * x * (1 - x)
    if x2 >= 1:
        print ("all dead")  # the population dies out because they all die
        data.append(x2)
        return data
    if x2<= 0:
        print ("all dead") # the population dies out because no new members are born
        data.append(x2)
        return data
    else:

        data.append(x2)


    try:
        logistic(x2, constant) # this is the recursive element, where the programme calls itself.

    except:
        print ("run out of puff") # the limit set above is exceeded
    return data[-1]

data = []

yvalue =[]
xvalue = []

for j in range (1,3999,1):
    j2 = float(j/1000)  # we plot across the range in intervals of 1/1000
    print (j2)
    value = logistic(0.5, j2) # 0.5 is the start value, but it is does not matter what value is chosen


    for i in range (1,100):
        yvalue.append(data[-i])
        xvalue.append(j2)
        plt.scatter(xvalue,yvalue,s=1) # plots the last 1000 points in the iteration to create the scatter diagram. This will take several hours to process.
plt.show()






